import json
import os

from src.data_prep import load_and_clean_data
from src.eda_analysis import (
    basic_overview,
    plot_distributions,
    correlation_analysis,
    trend_of_satisfaction,
    issue_vs_satisfaction,
    interaction_vs_satisfaction,
    activity_heatmap,
    wordcloud_transcripts,
    plot_category_counts
)

from src.insights import (
    insight_resolution_vs_satisfaction, 
    insight_issue_type_vs_satisfaction,
    insight_interaction_type_vs_issue,
    insight_interaction_type_vs_weekday,
    insight_resolution_time_by_issue,
    insight_resolution_time_vs_interaction,
    insight_issue_vs_weekday,
    insight_user_issue_journey,
    insight_customer_clustering
   )


if __name__ == "__main__":
    # Step 1 - Load and clean
    df = load_and_clean_data(
        path_raw="data/raw/Customer Interactions - Mohammad Sadegh MirShamsi - Sheet1.csv",
        save_path="data/processed/clean_interactions.csv"
    )

    # Step 2 - EDA
    basic_overview(df)                       
    plot_distributions(df)                    
    correlation_analysis(df)               
    trend_of_satisfaction(df, freq='W')      
    issue_vs_satisfaction(df)              
    interaction_vs_satisfaction(df)        
    activity_heatmap(df)                     
    wordcloud_transcripts(df)                  
    plot_category_counts(df)

    # --- Insights ---

def save_insight_result(result, save_dir="outputs/insight_reports/"):
    """
    Save each insight's result (summary + metadata) as JSON.
    """
    os.makedirs(save_dir, exist_ok=True)
    insight_name = result.get("insight_name", "unnamed_insight").replace(" ", "_").lower()
    file_path = os.path.join(save_dir, f"{insight_name}.json")

    def convert_keys(obj):
        if isinstance(obj, dict):
            return {str(k): convert_keys(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_keys(i) for i in obj]
        else:
            return obj

    result_clean = convert_keys(result)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(result_clean, f, indent=4, ensure_ascii=False)

    print(f"💾 Saved insight report → {file_path}")
    return file_path


def run_all_insights(df):
    """
    Run all insights and save each one separately.
    """
    insights = []

    insight_functions = [
        insight_resolution_vs_satisfaction,
        insight_issue_type_vs_satisfaction,
        insight_interaction_type_vs_issue,
        insight_interaction_type_vs_weekday,
        insight_resolution_time_by_issue,
        insight_resolution_time_vs_interaction,
        insight_issue_vs_weekday,
        insight_user_issue_journey,
        insight_customer_clustering
    ]

    print("\n💡 Running Insights...\n")

    for func in insight_functions:
        try:
            result = func(df)
            insights.append(result)
            save_insight_result(result)  
        except Exception as e:
            print(f"❌ Error in {func.__name__}: {e}")

    summary_path = "outputs/insight_reports/_all_insights_summary.json"
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(insights, f, indent=4, ensure_ascii=False)

    print(f"\n📘 Summary of all insights saved at: {summary_path}")
    return insights


insights_summary = run_all_insights(df)
