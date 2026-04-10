from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination

import pandas as pd

# Updated data for Loan Default Risk Prediction
data = pd.DataFrame(data = {
    'IncomeStability':['Stable','Stable','Unstable','Unstable','Stable','Unstable','Stable','Unstable'],
    'CreditHistory':['Good','Bad','Good','Bad','Good','Good','Bad','Bad'],
    'EmploymentType':['Salaried','Salaried','Self-employed','Unemployed','Salaried','Self-employed','Unemployed','Salaried'],
    'DefaultRisk':['Low','High','High','High','Low','High','High','High']
})

# Define the Bayesian Network structure for loan default risk
# Assuming IncomeStability, CreditHistory, and EmploymentType influence DefaultRisk
model = DiscreteBayesianNetwork([
    ('IncomeStability','DefaultRisk'),
    ('CreditHistory','DefaultRisk'),
    ('EmploymentType','DefaultRisk')
])

# Fit the model to the data to learn the Conditional Probability Distributions (CPDs)
model.fit(data)

print("Conditional Probability Distributions (CPDs):")
print(model.get_cpds())

# Perform inference using Variable Elimination
inference = VariableElimination(model)

# Query: Predict 'DefaultRisk' given 'IncomeStability' is 'Unstable' and 'CreditHistory' is 'Bad'
query_result = inference.query(
    variables=['DefaultRisk'],
    evidence={'IncomeStability':'Unstable', 'CreditHistory':'Bad'}
)

print("\nProbability of DefaultRisk given Unstable Income and Bad Credit History:")
print(query_result)