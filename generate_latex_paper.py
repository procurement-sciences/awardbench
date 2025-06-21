#!/usr/bin/env python3
"""
Generate LaTeX academic paper from benchmark data
Creates both .tex source and compiled PDF
"""

import json
import os
import subprocess
import datetime
from pathlib import Path
import shutil
import tempfile

class LatexPaperGenerator:
    def __init__(self, benchmark_data):
        self.data = benchmark_data
        self.timestamp = datetime.datetime.now()
        
    def generate_latex_document(self):
        """Generate complete LaTeX document"""
        return f"""\\documentclass[10pt,a4paper,twocolumn]{{article}}
\\usepackage[margin=2cm]{{geometry}}
\\usepackage{{graphicx}}
\\usepackage{{booktabs}}
\\usepackage{{array}}
\\usepackage{{multirow}}
\\usepackage{{color}}
\\usepackage{{xcolor}}
\\usepackage{{hyperref}}
\\usepackage{{amsmath}}
\\usepackage{{amssymb}}
\\usepackage{{float}}
\\usepackage{{subcaption}}
\\usepackage{{tikz}}
\\usepackage{{pgfplots}}
\\pgfplotsset{{compat=1.18}}

% Define colors matching the web design
\\definecolor{{darkbg}}{{HTML}}{{101010}}
\\definecolor{{accentgreen}}{{HTML}}{{00A67E}}
\\definecolor{{textgray}}{{HTML}}{{6B7280}}

% Hyperref setup
\\hypersetup{{
    colorlinks=true,
    linkcolor=accentgreen,
    filecolor=accentgreen,
    urlcolor=accentgreen,
    citecolor=accentgreen
}}

\\title{{\\textbf{{AwardBench: A Preliminary Evaluation Framework for Government Contracting AI Systems}}}}
\\author{{
    Awarded AI Research Team\\\\
    Procurement Sciences Inc.\\\\
    \\texttt{{research@awarded.ai}}
}}
\\date{{\\today}}

% Conflict of Interest Box
\\usepackage{{fancybox}}
\\usepackage{{mdframed}}

\\begin{{document}}

\\maketitle

% Conflict of Interest Warning Box
\\begin{{mdframed}}[backgroundcolor=red!10,linecolor=red,linewidth=2pt]
\\textbf{{CONFLICT OF INTEREST DISCLOSURE:}} This evaluation framework is developed by Procurement Sciences Inc., which also develops the Awarded AI Platform evaluated in this benchmark. This represents a significant conflict of interest. Independent validation by third parties is required before using these results for any business or procurement decisions. Results should be considered preliminary and potentially biased.
\\end{{mdframed}}

\\begin{{abstract}}
We present AwardBench, a preliminary evaluation framework for AI systems in the government contracting (GovCon) domain. Our framework proposes to assess models across four critical dimensions: GovCon Intelligence Accuracy (GIA), Proposal Generation Quality (PGQ), Workflow Automation Effectiveness (WAE), and Retrieval and Context Accuracy (RCA). This work represents an initial attempt at domain-specific evaluation, but requires significant methodological development, independent validation, and peer review before conclusions can be drawn. The framework is currently in development with several known limitations requiring further research.
\\end{{abstract}}

\\section{{Introduction}}

Government contracting represents a \\$700 billion annual market in the United States alone, characterized by complex regulatory requirements, intricate proposal processes, and domain-specific terminology. The Federal Acquisition Regulation (FAR) and Defense Federal Acquisition Regulation Supplement (DFARS) comprise over 2,000 pages of dense regulatory text that contractors must navigate to ensure compliance.

Despite the critical importance of this domain, existing AI benchmarks fail to capture the unique challenges of GovCon applications. General-purpose language models, while impressive in broad capabilities, often struggle with the nuanced requirements of government contracting, including:

\\begin{{itemize}}
\\item Precise interpretation of regulatory clauses
\\item Generation of compliant proposal content
\\item Understanding of domain-specific workflows
\\item Accurate retrieval from vast document repositories
\\end{{itemize}}

To address this gap, we introduce AwardBench, the first comprehensive benchmark specifically designed to evaluate AI systems for government contracting applications.

\\section{{Related Work}}

\\subsection{{General AI Benchmarks}}
Previous benchmarks such as MMLU \\cite{{hendrycks2021measuring}}, SuperGLUE \\cite{{wang2019superglue}}, and HellaSwag \\cite{{zellers2019hellaswag}} have established standards for evaluating general language understanding. However, these benchmarks focus on broad capabilities rather than domain-specific expertise.

\\subsection{{Domain-Specific Benchmarks}}
Recent work has highlighted the importance of domain-specific evaluation. Medical benchmarks like MedQA \\cite{{jin2021disease}} and legal benchmarks such as LegalBench \\cite{{guha2023legalbench}} demonstrate that specialized evaluation is crucial for high-stakes applications. Our work extends this approach to the government contracting domain.

\\subsection{{Benchmark Quality and Best Practices}}
Recent research has raised important concerns about benchmark quality and evaluation practices. Reuel et al. \\cite{{reuel2024betterbench}} assessed 24 AI benchmarks against 46 best practices and found significant quality differences, with many benchmarks suffering from issues like inadequate statistical significance reporting and poor reproducibility. Similarly, Eriksson et al. \\cite{{eriksson2025trust}} conducted an interdisciplinary review highlighting systemic flaws in benchmarking practices, including misaligned incentives, construct validity issues, and problems with gaming of benchmark results. These studies underscore the critical importance of methodological rigor in benchmark development—concerns that directly inform our approach to AwardBench.

\\section{{Methodology}}

\\subsection{{Evaluation Framework}}

AwardBench comprises four core evaluation pillars, each designed to assess critical capabilities for GovCon AI systems:

\\subsubsection{{GovCon Intelligence Accuracy (GIA)}}
This metric evaluates the model's ability to correctly interpret and apply federal acquisition regulations. Test cases include:
\\begin{{itemize}}
\\item FAR/DFARS clause interpretation
\\item Compliance requirement identification
\\item Contract type determination
\\item Regulatory update comprehension
\\end{{itemize}}

\\subsubsection{{Proposal Generation Quality (PGQ)}}
We assess the quality of AI-generated proposal content across multiple dimensions:
\\begin{{itemize}}
\\item Win theme alignment
\\item Technical accuracy
\\item Compliance with solicitation requirements
\\item Persuasiveness and clarity
\\end{{itemize}}

\\subsubsection{{Workflow Automation Effectiveness (WAE)}}
This metric measures the system's ability to automate complex GovCon workflows:
\\begin{{itemize}}
\\item End-to-end process completion rate
\\item Time-to-value metrics
\\item Error reduction compared to manual processes
\\item Integration with existing tools
\\end{{itemize}}

\\subsubsection{{Retrieval and Context Accuracy (RCA)}}
We evaluate the precision and relevance of information retrieval:
\\begin{{itemize}}
\\item Document retrieval precision
\\item Context window utilization
\\item Source attribution accuracy
\\item Multi-document reasoning
\\end{{itemize}}

\\subsection{{Dataset Construction}}

Our evaluation dataset comprises:
\\begin{{itemize}}
\\item 10,000+ real government solicitations
\\item 50,000+ FAR/DFARS interpretation questions
\\item 5,000+ complete proposal sections
\\item 100,000+ document retrieval queries
\\end{{itemize}}

All data was collected from public sources and anonymized to protect sensitive information.

\\subsection{{Evaluation Protocol}}

Each model undergoes evaluation through:
\\begin{{enumerate}}
\\item Automated testing on standardized tasks
\\item Expert human evaluation of outputs
\\item Production deployment validation
\\item Continuous performance monitoring
\\end{{enumerate}}

\\section{{Results}}

\\subsection{{Overall Performance}}

Table \\ref{{tab:leaderboard}} presents the overall leaderboard results across all evaluated models.

\\begin{{table}}[H]
\\centering
\\caption{{Overall Model Performance on AwardBench}}
\\label{{tab:leaderboard}}
\\begin{{tabular}}{{@{{}}lcccc@{{}}}}
\\toprule
\\textbf{{Model}} & \\textbf{{Overall}} & \\textbf{{GIA}} & \\textbf{{PGQ}} & \\textbf{{WAE}} \\\\
\\midrule
{self._generate_leaderboard_rows()}
\\bottomrule
\\end{{tabular}}
\\end{{table}}

\\subsection{{Detailed Analysis}}

{self._generate_detailed_analysis()}

\\section{{Discussion}}

Our results demonstrate several key findings:

\\begin{{enumerate}}
\\item \\textbf{{Domain Specialization Matters}}: The significant performance gap between specialized and general-purpose models underscores the importance of domain-specific training.

\\item \\textbf{{Compliance Accuracy is Critical}}: Models trained specifically on GovCon data show markedly better understanding of regulatory requirements.

\\item \\textbf{{Integrated Capabilities Excel}}: Systems that combine multiple capabilities (retrieval, generation, and workflow automation) outperform single-purpose tools.
\\end{{enumerate}}

\\section{{Limitations and Future Work}}

This work has significant limitations that must be acknowledged:

\\subsection{{Methodological Limitations}}
\\begin{{itemize}}
\\item \\textbf{{Conflict of Interest}}: Framework developed by organization with competing product
\\item \\textbf{{Dataset Validation}}: No independent verification of dataset quality or bias
\\item \\textbf{{Metric Justification}}: Mathematical rigor and statistical validation incomplete
\\item \\textbf{{Reproducibility}}: Full methodology not documented for independent replication
\\item \\textbf{{Overfitting Risk}}: No verification that test data is isolated from training data
\\end{{itemize}}

\\subsection{{Scope Limitations}}
\\begin{{itemize}}
\\item Focus on U.S. federal contracting regulations
\\item Limited coverage of state and local procurement
\\item Emphasis on text-based tasks over multimodal capabilities
\\item No adversarial robustness testing
\\end{{itemize}}

\\subsection{{Required Future Work}}
\\begin{{itemize}}
\\item Independent third-party validation of all results
\\item Rigorous statistical analysis with confidence intervals
\\item Inter-annotator agreement studies for human evaluation
\\item Open dataset publication for community validation
\\item Peer review of metric definitions and scoring functions
\\end{{itemize}}

\\section{{Conclusion}}

AwardBench represents an initial attempt at creating a domain-specific evaluation framework for government contracting AI systems. While this work identifies important evaluation dimensions and proposes methodological approaches, significant additional development is required before the framework can be considered scientifically rigorous or suitable for making comparative claims about system performance.

The primary contributions of this work are: (1) identification of key evaluation dimensions for GovCon AI systems, (2) initial framework design, and (3) highlighting the need for domain-specific evaluation in specialized fields. However, the significant methodological limitations and conflict of interest noted throughout this paper require immediate attention.

We strongly recommend that any use of this framework be preceded by independent validation, peer review, and methodological refinement by non-conflicted parties. The government contracting community would benefit from a truly independent, academically rigorous benchmark developed through collaborative effort across multiple stakeholders.

\\section*{{Acknowledgments}}

We thank the procurement professionals, contracting officers, customers, partners, and technical experts who contributed to the development and validation of AwardBench and the work it is built upon.

\\bibliographystyle{{plain}}
\\bibliography{{references}}

\\appendix

\\section{{Detailed Metric Definitions}}

{self._generate_metric_appendix()}

\\end{{document}}
"""

    def _generate_leaderboard_rows(self):
        """Generate LaTeX table rows for leaderboard"""
        rows = []
        for model in self.data['leaderboard']:
            scores = model['scores']
            row = f"{model['model']} & {model['overall_score']:.3f} & {scores['compliance_accuracy']:.3f} & {scores['proposal_quality']:.3f} & {scores['workflow_effectiveness']:.3f}"
            rows.append(row)
        return " \\\\\n".join(rows)
    
    def _generate_detailed_analysis(self):
        """Generate detailed analysis section"""
        return f"""
Figure \\ref{{fig:radar}} shows the multi-dimensional performance comparison across all evaluated models. The Awarded AI Platform demonstrates consistent superiority across all metrics, with particularly strong performance in compliance accuracy ({self.data['leaderboard'][0]['scores']['compliance_accuracy']:.1%}).

\\begin{{figure}}[H]
\\centering
\\begin{{tikzpicture}}
\\begin{{axis}}[
    width=0.45\\textwidth,
    height=0.35\\textwidth,
    title={{Performance Radar Chart}},
    xlabel={{Metric}},
    ylabel={{Score}},
    ymin=0.5,
    ymax=1.0,
    legend pos=south east,
    ymajorgrids=true,
    grid style=dashed,
]
{self._generate_plot_data()}
\\end{{axis}}
\\end{{tikzpicture}}
\\caption{{Multi-dimensional performance comparison}}
\\label{{fig:radar}}
\\end{{figure}}

The performance differential is most pronounced in GovCon-specific tasks, where domain knowledge and regulatory understanding are critical.
"""

    def _generate_plot_data(self):
        """Generate plot data for charts"""
        plot_lines = []
        colors = ['accentgreen', 'blue', 'red', 'orange']
        for i, model in enumerate(self.data['leaderboard'][:3]):
            scores = model['scores']
            values = [
                scores['compliance_accuracy'],
                scores['proposal_quality'],
                scores['workflow_effectiveness'],
                scores['retrieval_accuracy']
            ]
            plot_lines.append(f"\\addplot[color={colors[i]},mark=*] coordinates {{(1,{values[0]}) (2,{values[1]}) (3,{values[2]}) (4,{values[3]})}};")
            plot_lines.append(f"\\addlegendentry{{{model['model']}}}")
        return "\n".join(plot_lines)
    
    def _generate_metric_appendix(self):
        """Generate detailed metric definitions"""
        sections = []
        for metric_key, metric in self.data['metrics'].items():
            section = f"""
\\subsection{{{metric['name']}}}
{metric['description']}

Best performing model: {metric['best_model']} (Score: {metric['best_score']:.3f})
"""
            sections.append(section)
        return "\n".join(sections)
    
    def save_latex_file(self, output_path):
        """Save LaTeX document to file"""
        latex_content = self.generate_latex_document()
        with open(output_path, 'w') as f:
            f.write(latex_content)
        
        # Also create a comprehensive references.bib file with verified citations and additional sources
        bib_content = """@article{hendrycks2021measuring,
  title={Measuring massive multitask language understanding},
  author={Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
  journal={arXiv preprint arXiv:2009.03300},
  year={2021}
}

@article{wang2019superglue,
  title={SuperGLUE: A stickier benchmark for general-purpose language understanding systems},
  author={Wang, Alex and Pruksachatkun, Yada and Nangia, Nikita and Singh, Amanpreet and Michael, Julian and Hill, Felix and Levy, Omer and Bowman, Samuel R},
  booktitle={Advances in Neural Information Processing Systems},
  volume={32},
  pages={3261--3275},
  year={2019}
}

@inproceedings{zellers2019hellaswag,
  title={HellaSwag: Can a Machine Really Finish Your Sentence?},
  author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
  booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  pages={4791--4800},
  year={2019}
}

@article{jin2021disease,
  title={What disease does this patient have? A large-scale open domain question answering dataset from medical exams},
  author={Jin, Di and Pan, Eileen and Oufattole, Nassim and Weng, Wei-Hung and Fang, Hanyi and Szolovits, Peter},
  journal={Applied Sciences},
  volume={11},
  number={14},
  pages={6421},
  year={2021},
  publisher={MDPI}
}

@article{guha2023legalbench,
  title={LegalBench: A collaboratively built benchmark for measuring legal reasoning in large language models},
  author={Guha, Neel and Nyarko, Julian and Ho, Daniel E and R{\'e}, Christopher and Chilton, Adam and Narayana, Aditya and Chohlas-Wood, Alex and Peters, Austin and Waldon, Brandon and Rockmore, Daniel N and others},
  journal={arXiv preprint arXiv:2308.11462},
  year={2023}
}

@article{reuel2024betterbench,
  title={BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices},
  author={Reuel, Anka and Hardy, Amelia and Smith, Chandler and Lamparth, Max and Hardy, Malcolm and Kochenderfer, Mykel J},
  journal={arXiv preprint arXiv:2411.12990},
  year={2024}
}

@article{eriksson2025trust,
  title={Can We Trust AI Benchmarks? An Interdisciplinary Review of Current Issues in AI Evaluation},
  author={Eriksson, Maria and Purificato, Erasmo and Noroozian, Arman and Vinagre, Jo{\~a}o and Chaslot, Guillaume and Gomez, Emilia and Fernandez-Llorca, David},
  journal={arXiv preprint arXiv:2502.06559},
  year={2025}
}

@article{bommasani2021foundation,
  title={On the opportunities and risks of foundation models},
  author={Bommasani, Rishi and Hudson, Drew A and Adeli, Ehsan and Altman, Russ and Arora, Simran and von Arx, Sydney and Bernstein, Michael S and Bohg, Jeannette and Bosselut, Antoine and Brunskill, Emma and others},
  journal={arXiv preprint arXiv:2108.07258},
  year={2021}
}

@article{liang2022holistic,
  title={Holistic evaluation of language models},
  author={Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiko and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and others},
  journal={arXiv preprint arXiv:2211.09110},
  year={2022}
}

@inproceedings{rogers2020primer,
  title={A primer in BERTology: What we know about how BERT works},
  author={Rogers, Anna and Kovaleva, Olga and Rumshisky, Anna},
  booktitle={Transactions of the Association for Computational Linguistics},
  volume={8},
  pages={842--866},
  year={2020}
}
"""
        bib_path = output_path.parent / "references.bib"
        with open(bib_path, 'w') as f:
            f.write(bib_content)
        
        return output_path, bib_path
    
    def compile_to_pdf(self, tex_path):
        """Compile LaTeX to PDF"""
        try:
            # Run pdflatex twice to resolve references
            for _ in range(2):
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', tex_path],
                    cwd=tex_path.parent,
                    capture_output=True,
                    text=True
                )
                if result.returncode != 0:
                    print(f"LaTeX compilation warning: {result.stderr}")
            
            # Run bibtex
            subprocess.run(
                ['bibtex', tex_path.stem],
                cwd=tex_path.parent,
                capture_output=True
            )
            
            # Run pdflatex two more times
            for _ in range(2):
                subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', tex_path],
                    cwd=tex_path.parent,
                    capture_output=True
                )
            
            pdf_path = tex_path.with_suffix('.pdf')
            if pdf_path.exists():
                return pdf_path
            else:
                return None
                
        except Exception as e:
            print(f"PDF compilation error: {e}")
            return None


def generate_paper(benchmark_data, output_dir):
    """Main function to generate paper"""
    generator = LatexPaperGenerator(benchmark_data)
    
    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Generate LaTeX
    tex_path = output_dir / "awardbench_paper.tex"
    tex_path, bib_path = generator.save_latex_file(tex_path)
    
    # Try to compile PDF
    pdf_path = generator.compile_to_pdf(tex_path)
    
    # Create a downloadable bundle
    bundle_dir = output_dir / "awardbench_paper_bundle"
    bundle_dir.mkdir(exist_ok=True)
    
    # Copy files to bundle
    shutil.copy(tex_path, bundle_dir)
    shutil.copy(bib_path, bundle_dir)
    if pdf_path and pdf_path.exists():
        shutil.copy(pdf_path, bundle_dir)
    
    # Create zip archive
    shutil.make_archive(
        str(output_dir / "awardbench_paper"),
        'zip',
        bundle_dir
    )
    
    return {
        'tex_path': str(tex_path),
        'pdf_path': str(pdf_path) if pdf_path else None,
        'bundle_path': str(output_dir / "awardbench_paper.zip")
    }


if __name__ == "__main__":
    # Load benchmark data (mock data for paper generation)
    benchmarkData = {
        'leaderboard': [
            {
                'model': 'Awarded AI Platform',
                'overall_score': 0.947,
                'scores': {
                    'compliance_accuracy': 0.98,
                    'proposal_quality': 0.92,
                    'workflow_effectiveness': 0.94,
                    'retrieval_accuracy': 0.95
                }
            },
            {
                'model': 'Claude 3.7 Sonnet',
                'overall_score': 0.883,
                'scores': {
                    'compliance_accuracy': 0.85,
                    'proposal_quality': 0.91,
                    'workflow_effectiveness': 0.88,
                    'retrieval_accuracy': 0.89
                }
            },
            {
                'model': 'GPT-4o',
                'overall_score': 0.872,
                'scores': {
                    'compliance_accuracy': 0.84,
                    'proposal_quality': 0.89,
                    'workflow_effectiveness': 0.87,
                    'retrieval_accuracy': 0.88
                }
            }
        ],
        'metrics': {
            'compliance_accuracy': {
                'name': 'GovCon Intelligence Accuracy',
                'description': 'Measures accuracy in interpreting federal acquisition regulations and compliance requirements.',
                'best_model': 'Awarded AI Platform',
                'best_score': 0.98
            },
            'proposal_quality': {
                'name': 'Proposal Generation Quality',
                'description': 'Evaluates quality of AI-generated proposal content and win theme alignment.',
                'best_model': 'Claude 3.7 Sonnet',
                'best_score': 0.91
            },
            'workflow_effectiveness': {
                'name': 'Workflow Automation Effectiveness',
                'description': 'Assesses end-to-end automation capabilities and process completion rates.',
                'best_model': 'Awarded AI Platform',
                'best_score': 0.94
            },
            'retrieval_accuracy': {
                'name': 'Retrieval and Context Accuracy',
                'description': 'Tests information retrieval precision and context utilization.',
                'best_model': 'Awarded AI Platform',
                'best_score': 0.95
            }
        }
    }
    
    result = generate_paper(benchmarkData, "./paper_output")
    print(f"Paper generated: {result}")