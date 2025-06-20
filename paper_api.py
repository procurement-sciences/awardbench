#!/usr/bin/env python3
"""
API endpoint for generating academic papers
"""

from flask import Flask, jsonify, send_file, make_response
from flask_cors import CORS
import json
import os
from pathlib import Path
from generate_latex_paper import generate_paper
import tempfile
import shutil

app = Flask(__name__)
CORS(app)

# Load benchmark data
def load_benchmark_data():
    """Load current benchmark data"""
    # In production, this would fetch from database
    return {
        "timestamp": "2025-01-20T12:00:00Z",
        "leaderboard": [
            {
                "rank": 1,
                "model": "Awarded AI Platform",
                "overall_score": 0.947,
                "grade": "A+",
                "scores": {
                    "compliance_accuracy": 0.98,
                    "proposal_quality": 0.92,
                    "workflow_effectiveness": 0.94,
                    "retrieval_accuracy": 0.95,
                    "efficiency": 0.96,
                },
                "strengths": [
                    "Exceptional compliance accuracy",
                    "Superior domain knowledge",
                ],
            },
            {
                "rank": 2,
                "model": "Claude 3.7 Sonnet",
                "overall_score": 0.883,
                "grade": "A",
                "scores": {
                    "compliance_accuracy": 0.85,
                    "proposal_quality": 0.91,
                    "workflow_effectiveness": 0.88,
                    "retrieval_accuracy": 0.89,
                    "efficiency": 0.9,
                },
                "strengths": ["Strong proposal generation", "Good efficiency"],
            },
            {
                "rank": 3,
                "model": "GPT-4o",
                "overall_score": 0.872,
                "grade": "A",
                "scores": {
                    "compliance_accuracy": 0.83,
                    "proposal_quality": 0.89,
                    "workflow_effectiveness": 0.87,
                    "retrieval_accuracy": 0.88,
                    "efficiency": 0.89,
                },
                "strengths": ["Consistent performance", "Fast response times"],
            },
        ],
        "metrics": {
            "compliance_accuracy": {
                "name": "Compliance Accuracy",
                "description": "FAR/DFARS interpretation and compliance requirement identification",
                "best_model": "Awarded AI Platform",
                "best_score": 0.98,
            },
            "proposal_quality": {
                "name": "Proposal Generation Quality",
                "description": "Win theme alignment and technical accuracy in proposals",
                "best_model": "Awarded AI Platform",
                "best_score": 0.92,
            },
            "workflow_effectiveness": {
                "name": "Workflow Automation",
                "description": "End-to-end process automation and time-to-value",
                "best_model": "Awarded AI Platform",
                "best_score": 0.94,
            },
            "retrieval_accuracy": {
                "name": "Retrieval & Context",
                "description": "Document retrieval precision and context utilization",
                "best_model": "Awarded AI Platform",
                "best_score": 0.95,
            },
            "efficiency": {
                "name": "Overall Efficiency",
                "description": "Speed, cost optimization, and resource utilization",
                "best_model": "Awarded AI Platform",
                "best_score": 0.96,
            },
        },
    }

@app.route('/api/paper/generate', methods=['GET'])
def generate_paper_endpoint():
    """Generate academic paper on demand"""
    try:
        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Load current data
            benchmark_data = load_benchmark_data()
            
            # Generate paper
            result = generate_paper(benchmark_data, temp_dir)
            
            # Prepare response
            response_data = {
                'status': 'success',
                'generated_at': benchmark_data['timestamp'],
                'files': {
                    'tex': result['tex_path'] is not None,
                    'pdf': result['pdf_path'] is not None,
                    'bundle': result['bundle_path'] is not None
                }
            }
            
            # Copy files to permanent location
            output_dir = Path('./paper_output')
            output_dir.mkdir(exist_ok=True)
            
            if result['tex_path']:
                shutil.copy(result['tex_path'], output_dir / 'awardbench_paper.tex')
            if result['pdf_path']:
                shutil.copy(result['pdf_path'], output_dir / 'awardbench_paper.pdf')
            if result['bundle_path']:
                shutil.copy(result['bundle_path'], output_dir / 'awardbench_paper.zip')
            
            return jsonify(response_data)
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/paper/download/<format>', methods=['GET'])
def download_paper(format):
    """Download paper in specified format"""
    try:
        output_dir = Path('./paper_output')
        
        if format == 'tex':
            file_path = output_dir / 'awardbench_paper.tex'
            mimetype = 'text/plain'
            download_name = 'awardbench_paper.tex'
        elif format == 'pdf':
            file_path = output_dir / 'awardbench_paper.pdf'
            mimetype = 'application/pdf'
            download_name = 'awardbench_paper.pdf'
        elif format == 'bundle':
            file_path = output_dir / 'awardbench_paper.zip'
            mimetype = 'application/zip'
            download_name = 'awardbench_paper_bundle.zip'
        else:
            return jsonify({'error': 'Invalid format'}), 400
        
        if not file_path.exists():
            # Generate paper if not exists
            benchmark_data = load_benchmark_data()
            generate_paper(benchmark_data, output_dir)
            
            if not file_path.exists():
                return jsonify({'error': 'File generation failed'}), 500
        
        return send_file(
            file_path,
            mimetype=mimetype,
            as_attachment=True,
            download_name=download_name
        )
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/paper/status', methods=['GET'])
def paper_status():
    """Check paper generation status"""
    output_dir = Path('./paper_output')
    
    return jsonify({
        'tex_available': (output_dir / 'awardbench_paper.tex').exists(),
        'pdf_available': (output_dir / 'awardbench_paper.pdf').exists(),
        'bundle_available': (output_dir / 'awardbench_paper.zip').exists(),
        'last_updated': load_benchmark_data()['timestamp']
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)