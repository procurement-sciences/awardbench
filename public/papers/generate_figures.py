import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Define colors matching the LaTeX document
DARK_GREEN = '#00A67E'
DARK_BLUE = '#3B82F6'
DARK_RED = '#EF4444'
DARK_YELLOW = '#F59E0B'

# Figure 1: Test Case Distribution
def create_test_distribution():
    dimensions = ['Compliance\nAccuracy', 'Proposal\nQuality', 'Workflow\nEffectiveness', 
                  'Retrieval\nAccuracy', 'Overall\nEfficiency']
    test_cases = [2584, 2156, 1947, 2103, 2057]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dimensions, test_cases, color=DARK_GREEN, edgecolor='black', linewidth=1.5)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylabel('Number of Test Cases', fontsize=14, fontweight='bold')
    ax.set_xlabel('Evaluation Dimension', fontsize=14, fontweight='bold')
    ax.set_title('Distribution of Test Cases Across Evaluation Dimensions', fontsize=16, fontweight='bold')
    ax.set_ylim(0, 3000)
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    plt.tight_layout()
    plt.savefig('figure_test_distribution.pdf', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 2: Overall Performance Scores
def create_overall_performance():
    models = ['Generic ChatGPT', 'Llama 3.1 70B', 'Mistral Large', 'Command R+', 
              'Gemini 1.5 Pro', 'Claude 3 Haiku', 'GPT-4 Turbo', 'Claude 3.5 Sonnet', 
              'GPT-4o', 'Claude 3 Opus', 'Awarded AI Platform']
    scores = [72.4, 74.2, 76.4, 78.9, 82.3, 84.1, 85.6, 88.3, 87.2, 91.2, 94.7]
    colors = [DARK_RED]*4 + [DARK_BLUE]*6 + [DARK_GREEN]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    bars = ax.barh(models, scores, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax.text(score + 0.5, bar.get_y() + bar.get_height()/2.,
                f'{score}%', ha='left', va='center', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('Overall Score (%)', fontsize=14, fontweight='bold')
    ax.set_title('Overall Performance Scores Across Evaluated Models', fontsize=16, fontweight='bold')
    ax.set_xlim(60, 100)
    
    # Add performance tier annotations
    ax.axvspan(90, 100, alpha=0.1, color=DARK_GREEN, label='Elite Performance')
    ax.axvspan(80, 90, alpha=0.1, color=DARK_BLUE, label='Advanced Capability')
    ax.axvspan(70, 80, alpha=0.1, color=DARK_YELLOW, label='Professional Standard')
    
    ax.legend(loc='lower right', framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle='--', axis='x')
    
    plt.tight_layout()
    plt.savefig('figure_overall_performance.pdf', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 3: Compliance Accuracy Radar Chart
def create_compliance_radar():
    categories = ['FAR Basic', 'FAR Complex', 'DFARS', 'Agency-Specific', 'Multi-doc']
    
    # Data for each model
    awarded_ai = [99.2, 97.8, 96.4, 95.1, 93.7]
    claude_opus = [94.3, 88.7, 82.1, 78.4, 75.2]
    gpt4o = [92.1, 85.4, 79.3, 74.2, 71.8]
    generic = [78.4, 61.2, 52.3, 45.7, 42.1]
    
    # Number of variables
    N = len(categories)
    
    # Compute angle for each axis
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    # Initialize the plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    # Draw data
    for data, color, label in [(awarded_ai, DARK_GREEN, 'Awarded AI Platform'),
                                (claude_opus, DARK_BLUE, 'Claude 3 Opus'),
                                (gpt4o, DARK_YELLOW, 'GPT-4o'),
                                (generic, DARK_RED, 'Generic ChatGPT')]:
        values = data + data[:1]
        ax.plot(angles, values, 'o-', linewidth=2, color=color, label=label)
        ax.fill(angles, values, alpha=0.15, color=color)
    
    # Fix axis to go in the right order and start at 12 o'clock
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw axis lines for each angle and label
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=12)
    
    # Set y-axis limits and labels
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], size=10)
    
    # Add title and legend
    ax.set_title('Compliance Accuracy Across Different Regulation Types', 
                 size=16, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), framealpha=0.9)
    
    ax.grid(True)
    plt.tight_layout()
    plt.savefig('figure_compliance_radar.pdf', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 4: Processing Time Scaling
def create_efficiency_plots():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Processing time subplot
    input_sizes = [10, 50, 100, 200, 500]
    awarded_times = [2.3, 5.8, 9.2, 15.7, 32.4]
    gpt4o_times = [3.1, 12.4, 24.8, 48.2, 112.3]
    generic_times = [4.7, 18.9, 38.2, 74.3, 178.9]
    
    ax1.plot(input_sizes, awarded_times, 'o-', color=DARK_GREEN, linewidth=2.5, 
             markersize=8, label='Awarded AI')
    ax1.plot(input_sizes, gpt4o_times, 's-', color=DARK_BLUE, linewidth=2, 
             markersize=7, label='GPT-4o')
    ax1.plot(input_sizes, generic_times, '^-', color=DARK_RED, linewidth=2, 
             markersize=7, label='Generic ChatGPT')
    
    ax1.set_xlabel('Input Size (pages)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Processing Time (seconds)', fontsize=12, fontweight='bold')
    ax1.set_title('Processing Time Scaling', fontsize=14, fontweight='bold')
    ax1.legend(framealpha=0.9)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_xlim(0, 550)
    ax1.set_ylim(0, 200)
    
    # Reliability under load subplot
    concurrent_requests = [1, 10, 50, 100, 200]
    awarded_reliability = [99.8, 99.2, 98.4, 97.1, 95.3]
    gpt4o_reliability = [98.7, 95.3, 88.2, 79.4, 64.7]
    generic_reliability = [96.2, 87.4, 71.3, 52.8, 31.2]
    
    ax2.plot(concurrent_requests, awarded_reliability, 'o-', color=DARK_GREEN, 
             linewidth=2.5, markersize=8, label='Awarded AI')
    ax2.plot(concurrent_requests, gpt4o_reliability, 's-', color=DARK_BLUE, 
             linewidth=2, markersize=7, label='GPT-4o')
    ax2.plot(concurrent_requests, generic_reliability, '^-', color=DARK_RED, 
             linewidth=2, markersize=7, label='Generic ChatGPT')
    
    ax2.set_xlabel('Concurrent Requests', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Success Rate (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Reliability Under Load', fontsize=14, fontweight='bold')
    ax2.legend(loc='lower left', framealpha=0.9)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_xlim(0, 220)
    ax2.set_ylim(20, 105)
    
    plt.tight_layout()
    plt.savefig('figure_efficiency_plots.pdf', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 5: Error Analysis Heatmap
def create_error_heatmap():
    error_types = ['Regulatory\nMisinterpretation', 'Context Window\nOverflow', 
                   'Hallucinated\nRequirements', 'Inconsistent\nResponses', 
                   'Formatting\nErrors']
    models = ['Awarded AI', 'Claude 3 Opus', 'GPT-4o', 'Generic ChatGPT']
    
    # Error rates (percentages)
    error_data = np.array([
        [2.1, 1.3, 0.8, 3.2, 4.1],   # Awarded AI
        [5.2, 2.8, 2.1, 5.4, 5.8],   # Claude 3 Opus
        [8.7, 4.3, 5.6, 9.2, 6.4],   # GPT-4o
        [18.4, 8.7, 12.3, 15.6, 7.2]  # Generic ChatGPT
    ])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(error_data, cmap='YlOrRd', aspect='auto')
    
    # Set ticks and labels
    ax.set_xticks(np.arange(len(error_types)))
    ax.set_yticks(np.arange(len(models)))
    ax.set_xticklabels(error_types, fontsize=11)
    ax.set_yticklabels(models, fontsize=12)
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center")
    
    # Add colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Error Rate (%)', rotation=90, va="bottom", fontsize=12)
    
    # Add text annotations
    for i in range(len(models)):
        for j in range(len(error_types)):
            text = ax.text(j, i, f'{error_data[i, j]:.1f}%',
                          ha="center", va="center", color="black" if error_data[i, j] < 10 else "white",
                          fontweight='bold', fontsize=10)
    
    ax.set_title("Error Rates by Type and Model", fontsize=16, fontweight='bold', pad=20)
    fig.tight_layout()
    plt.savefig('figure_error_heatmap.pdf', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 6: ROI Projection Chart
def create_roi_projection():
    months = np.arange(0, 13)
    
    # Costs and revenues (in thousands)
    implementation_cost = 150  # One-time cost
    monthly_operational = 10   # Ongoing cost
    
    # Calculate cumulative costs
    cumulative_costs = implementation_cost + months * monthly_operational
    
    # Calculate cumulative revenues (based on increased win rates and proposal volume)
    base_monthly_revenue = 0
    ai_enhanced_revenue = months * 65  # Average monthly benefit
    ai_enhanced_revenue[0] = 0  # No revenue in month 0
    
    # Calculate ROI
    roi = ((ai_enhanced_revenue - cumulative_costs) / implementation_cost) * 100
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
    
    # Revenue/Cost subplot
    ax1.plot(months, cumulative_costs, 'o-', color=DARK_RED, linewidth=2.5, 
             markersize=8, label='Cumulative Costs')
    ax1.plot(months, ai_enhanced_revenue, 's-', color=DARK_GREEN, linewidth=2.5, 
             markersize=8, label='Cumulative Revenue')
    ax1.fill_between(months, cumulative_costs, ai_enhanced_revenue, 
                     where=(ai_enhanced_revenue >= cumulative_costs), 
                     color=DARK_GREEN, alpha=0.3, label='Profit')
    ax1.fill_between(months, cumulative_costs, ai_enhanced_revenue, 
                     where=(ai_enhanced_revenue < cumulative_costs), 
                     color=DARK_RED, alpha=0.3, label='Investment')
    
    ax1.set_ylabel('Amount ($1000s)', fontsize=12, fontweight='bold')
    ax1.set_title('AI Implementation Financial Analysis', fontsize=16, fontweight='bold')
    ax1.legend(loc='upper left', framealpha=0.9)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_ylim(-50, 800)
    
    # ROI subplot
    ax2.plot(months, roi, 'o-', color=DARK_BLUE, linewidth=3, markersize=8)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax2.axhline(y=100, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    ax2.axhline(y=340, color=DARK_GREEN, linestyle='--', linewidth=2, alpha=0.7)
    ax2.fill_between(months, 0, roi, where=(roi > 0), color=DARK_GREEN, alpha=0.3)
    ax2.fill_between(months, 0, roi, where=(roi <= 0), color=DARK_RED, alpha=0.3)
    
    # Add annotations
    ax2.text(11, 350, '340% Target', ha='left', va='bottom', fontsize=10, 
             color=DARK_GREEN, fontweight='bold')
    
    # Find breakeven point
    breakeven_month = np.where(roi > 0)[0][0] if any(roi > 0) else None
    if breakeven_month:
        ax2.plot(breakeven_month, roi[breakeven_month], 'o', color='red', 
                markersize=12, markeredgecolor='black', markeredgewidth=2)
        ax2.text(breakeven_month, roi[breakeven_month] - 30, 
                f'Breakeven\nMonth {breakeven_month}', 
                ha='center', va='top', fontsize=10, fontweight='bold')
    
    ax2.set_xlabel('Months After Implementation', fontsize=12, fontweight='bold')
    ax2.set_ylabel('ROI (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Return on Investment Projection', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_ylim(-100, 450)
    
    plt.tight_layout()
    plt.savefig('figure_roi_projection.pdf', dpi=300, bbox_inches='tight')
    plt.close()

# Generate all figures
if __name__ == "__main__":
    print("Generating figures for AwardBench paper...")
    
    create_test_distribution()
    print("✓ Test distribution figure created")
    
    create_overall_performance()
    print("✓ Overall performance figure created")
    
    create_compliance_radar()
    print("✓ Compliance radar chart created")
    
    create_efficiency_plots()
    print("✓ Efficiency plots created")
    
    create_error_heatmap()
    print("✓ Error heatmap created")
    
    create_roi_projection()
    print("✓ ROI projection chart created")
    
    print("\nAll figures generated successfully!")