# AwardBench - Government Contracting AI Evaluation Framework

## Overview

AwardBench is an evaluation framework for AI systems in the government contracting (GovCon) domain. It provides benchmarks that measure AI performance across critical GovCon-specific tasks including compliance checking, proposal generation, and workflow automation.

## ⚠️ Important Disclaimers

### Conflict of Interest

This evaluation framework is developed by Procurement Sciences Inc., which also develops the Awarded AI Platform - one of the systems being evaluated in this benchmark. This represents a significant conflict of interest that must be acknowledged in all presentations of results. **Independent validation by third parties is strongly recommended before making any procurement or business decisions based on these results.**

### Development Status

This framework is currently **IN PROGRESS** and should be considered experimental. Several critical components require further development, validation, and independent review before the framework can be considered scientifically rigorous.

### Known Limitations

- Dataset curation methodology needs independent validation
- Metric definitions require peer review and statistical justification
- Inter-annotator agreement protocols are incomplete
- Reproducibility standards are not fully implemented
- Independent third-party validation is pending

## Quick Start

### Prerequisites

```bash
# Node.js and npm
node --version  # v18+ required

# Python (for visualizations)
python --version  # 3.8+ required

# Environment variables
cp .env.example .env
# Add your API keys to .env:
# - LANGSMITH_API_KEY
# - LANGSMITH_ENDPOINT (optional, defaults to cloud)
# - SUPABASE_URL (for production data sampling)
# - SUPABASE_ANON_KEY or SUPABASE_SERVICE_KEY
```

### Installation

```bash
# Install dependencies
npm install

# Install Python dependencies for visualizations
pip install -r evaluations/requirements.txt
```

### Running Evaluations

```bash
# Create evaluation datasets in LangSmith
npm run eval:create-datasets

# Run full evaluation suite
npm run eval:run

# Generate benchmark visualizations
npm run eval:visualize

# Run production data sampling (optional)
npm run eval:sample-production
```

## Architecture

### Core Components

1. **Evaluation Framework** (`AWARDED_AI_EVALUATION_FRAMEWORK.md`)

   - Defines 5 evaluation pillars: GIA, PGQ, WAE, RCA, MMI
   - Establishes methodology and success metrics

2. **LangSmith Integration** (`langsmith/`)

   - `config.ts`: Configuration and API setup
   - `create-datasets.ts`: Dataset creation scripts
   - `evaluators.ts`: Custom evaluator implementations
   - `run-evaluations.ts`: Evaluation execution pipeline

3. **Production Data Sampling** (`data-sampling/`)

   - Anonymized production data collection
   - Quality filtering and categorization
   - Privacy-preserving sampling

4. **Benchmark Suite** (`benchmark-suite/`)
   - Interactive web dashboard
   - Academic-quality visualizations
   - Publication-ready charts

## Evaluation Metrics

### 1. GovCon Intelligence Accuracy (GIA)

- FAR/DFARS compliance checking
- Contract clause interpretation
- Regulatory requirement identification

### 2. Proposal Generation Quality (PGQ)

- Win theme alignment
- Technical accuracy
- Past performance integration

### 3. Workflow Automation Effectiveness (WAE)

- End-to-end process completion
- Time-to-value metrics
- Error recovery capabilities

### 4. Retrieval and Context Accuracy (RCA)

- Document retrieval precision
- Context window utilization
- Source attribution accuracy

### 5. Multi-Model Intelligence (MMI)

- Model selection accuracy
- Cost optimization
- Response quality consistency

## Adding New Evaluations

### 1. Create a New Dataset

```typescript
// In langsmith/create-datasets.ts
export async function createYourDataset() {
  const datasetName = 'your-dataset-name';
  const dataset = await langsmithClient.createDataset(datasetName, {
    description: 'Your dataset description',
    dataType: 'kv',
  });

  // Add examples
  const examples = [
    {
      input: {
        /* your input */
      },
      output: {
        /* expected output */
      },
      metadata: {
        /* metadata */
      },
    },
  ];

  for (const example of examples) {
    await langsmithClient.createExample(example.input, example.output, {
      datasetId: dataset.id,
      metadata: example.metadata,
    });
  }
}
```

### 2. Create a Custom Evaluator

```typescript
// In langsmith/evaluators.ts
export class YourCustomEvaluator extends RunEvaluator {
  evaluatorType = 'scorer' as const;

  async evaluateRun(run: Run, example: Example): Promise<EvaluationResult> {
    // Your evaluation logic
    const score = calculateScore(run.outputs, example.outputs);

    return {
      key: 'your_metric_name',
      score,
      comment: `Evaluation details...`,
    };
  }
}
```

### 3. Add to Evaluation Pipeline

```typescript
// In langsmith/run-evaluations.ts
const evaluators = [...existingEvaluators, new YourCustomEvaluator()];
```

## Reproducibility Guide

### 1. Environment Setup

```bash
# Use exact versions
npm ci  # Install from package-lock.json

# Set consistent random seeds
export RANDOM_SEED=42
```

### 2. Data Versioning

All datasets are versioned in LangSmith with timestamps. To reproduce exact results:

```typescript
// Use specific dataset versions
const datasetVersion = '2025-06-20T10:00:00Z';
const dataset = await langsmithClient.readDataset({
  datasetName: 'govcon-qa-benchmark-v1',
  asOf: datasetVersion,
});
```

### 3. Model Configuration

```typescript
// In evaluations/models.config.ts
export const MODEL_CONFIGS = {
  'gpt-4o': {
    temperature: 0.0, // Deterministic
    max_tokens: 2000,
    seed: 42,
  },
  'claude-3.7-sonnet': {
    temperature: 0.0,
    max_tokens: 2000,
  },
};
```

## Publishing Results

### 1. Generate Report

```bash
# Generate comprehensive report
npm run eval:report

# Output:
# - evaluations/reports/awardbench-report-[timestamp].json
# - evaluations/reports/awardbench-report-[timestamp].md
```

### 2. Create Visualizations

```bash
# Generate publication-ready charts
cd evaluations/benchmark-suite
python generate_visuals.py

# Output in visualizations/:
# - main_comparison.pdf/png
# - radar_comparison.pdf/png
# - performance_heatmap.pdf/png
# - superiority_margins.pdf/png
# - academic_summary.pdf/png
```

### 3. Deploy Dashboard

```bash
# Serve locally
cd evaluations/benchmark-suite
python -m http.server 8000

# Or deploy to static hosting
# Copy benchmark-suite/ to your static host
```

### 4. Academic Publication

The framework generates LaTeX-ready figures and tables:

```latex
\begin{figure}[h]
  \centering
  \includegraphics[width=\textwidth]{academic_summary.pdf}
  \caption{AwardBench comprehensive evaluation results}
  \label{fig:awardbench}
\end{figure}
```

## Continuous Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/evaluations.yml
name: Run AwardBench Evaluations

on:
  schedule:
    - cron: '0 0 * * *' # Daily
  push:
    branches: [main]

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run eval:run
      - uses: actions/upload-artifact@v3
        with:
          name: evaluation-reports
          path: evaluations/reports/
```

## API Usage

### Programmatic Access

```typescript
import { runEvaluation } from './evaluations/langsmith/run-evaluations';
import { AwardBenchConfig } from './evaluations/types';

const config: AwardBenchConfig = {
  models: ['gpt-4o', 'claude-3.7-sonnet'],
  datasets: ['govcon-qa-benchmark-v1'],
  evaluators: ['compliance_accuracy', 'proposal_quality'],
  parallel: true,
};

const results = await runEvaluation(config);
console.log(results.leaderboard);
```

### REST API Endpoints

```bash
# Get latest benchmark results
GET /api/v1/benchmarks/latest

# Get specific evaluation run
GET /api/v1/evaluations/:runId

# Submit model for evaluation
POST /api/v1/evaluate
{
  "model": "your-model-id",
  "provider": "your-provider",
  "datasets": ["govcon-qa-benchmark-v1"]
}
```

## Best Practices

### 1. Evaluation Design

- Use stratified sampling for balanced datasets
- Include edge cases and adversarial examples
- Validate with human expert review

### 2. Statistical Rigor

- Report confidence intervals
- Use appropriate statistical tests
- Account for multiple comparisons

### 3. Ethical Considerations

- Anonymize all production data
- Remove PII and sensitive information
- Respect data retention policies

## Troubleshooting

### Common Issues

1. **LangSmith Connection Error**

   ```bash
   # Verify credentials
   curl -H "X-API-Key: $LANGSMITH_API_KEY" \
        https://api.langsmith.com/api/v1/info
   ```

2. **Memory Issues with Large Datasets**

   ```bash
   # Increase Node.js memory
   NODE_OPTIONS="--max-old-space-size=8192" npm run eval:run
   ```

3. **Visualization Errors**

   ```bash
   # Install system dependencies
   # macOS
   brew install python-tk

   # Ubuntu
   sudo apt-get install python3-tk
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new evaluators
4. Submit a pull request

### Code Standards

- TypeScript strict mode
- 100% test coverage for evaluators
- Documentation for all public APIs

## License

Copyright 2025 Procurement Sciences Inc. All rights reserved.

## Contact

- **Technical Support**: engineering@awarded.ai
- **Research Collaboration**: research@awarded.ai
- **General Inquiries**: info@awarded.ai

## Citation

If you use AwardBench in your research, please cite:

```bibtex
@misc{awardbench2025,
  title={AwardBench: A Comprehensive Evaluation Framework for Government Contracting AI},
  author={Awarded AI Research Team},
  year={2025},
  publisher={Procurement Sciences Inc.},
  howpublished={\url{https://github.com/awarded-ai/awardbench}}
}
```
