import json
from .getMentalnsights import get_top_three_correllations


def lambda_handler(event, context):
    try:
        top_three_correlatations = get_top_three_correllations
        output = { 
            "top_stress_features": [item for item in top_three_correlatations],
            "correlations": dict(coef)
        }

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(output),
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
