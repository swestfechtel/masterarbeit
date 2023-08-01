# masterarbeit

readme only contains working notes ;-)

## Notes:
- in bucharest dataset, the event dataset contains all contact nominations. The patient dataset contains all
patients who have been recorded as positive. All referees from the event dataset are contained in the patient dataset.
However, only some referrals are contained in the patient dataset, and not all patients are also recorded as referees.
    - referees ⊆ patients
    - referrals = A ∪ B; A ⊆ patients, B ⊄ patients
    - patients = referees ∪ A ∪ C; C ⊅ referees, C ⊅ referrals

- REM node attribute covariates can be source-level, target-level, and source-target-relation level
- RHEM node attribute covariates can either be source-receiver set relation level

## REM Covariates:
### Note attributes:
- age difference
- sex difference
- residency difference (where applicable)
- job difference (where applicable)
- more from big china dataset

### Network effects
- repetition:
  - A ---> B t_n
  
    A ---> B t_n+1
- nomination activity
  - A ---> B t_n
    
    A ---> X t_n+1
- exact reciprocity:
  - A ---> B t_n
    
    A <--- B t_n+1
- reciprocity
  - A ---> B t_n
  
    X <--- B t_n+1
- cyclical tie:
  - A (OUT) ---> X t_n
  
    X ---> B (IN) t_n
  
    B ---> A t_n+1
- transitive tie:
  - A (IN) ---> X t_n
  
    X (OUT) ---> B t_n
  
    A ---> B t_n+1
- triangle effect children:
  - A ---> B (IN) t_n
  
    A ---> C (IN) t_n
  
    B <--> C t_n+1
- triangle effect parents:
  - A (OUT) ---> C t_n
  
    B (OUT) ---> C t_n
  
    A <--> B t_n+1
## RHEM covariates:
### Node attributes

- age difference: DIR_HYPEREDGE_PARTICIPANT_COVAR_DIFF_STATISTIC
- sex difference: DIR_HYPEREDGE_PARTICIPANT_COVAR_DIFF_STATISTIC
- average age: DIR_HYPEREDGE_PARTICIPANT_COVAR_AVG_STATISTIC
- categorical attributes: DIR_HYPEREDGE_PARTICIPANT_CAT_COVAR_DIFF_STATISTIC
### Network effects

- exact repetition: (UN)DIR_HYPEREDGE_REPETITION_STATISTIC
  - A ---> B,C t_n
  
    A ---> B,C t_n+1
- partial repetition: DIR_HYPEREDGE_SUB_REPETITION_STATISTIC_AVG
  - A ---> B,C t_n
  
    A ---> B,D t_n+1
- unordered repetition: DIR_HYPEREDGE_UNDIRECTED_REPETITION_STATISTIC
  - A ---> B,C t_n
  
    B ---> A,C t_n+1
- unordered partial repetition: DIR_HYPEREDGE_SUB_REPETITION_STATISTIC_AVG
  - A ---> B,C t_n
  
    B ---> A,D t_n+1
- generalised reciprocation: DIR_HYPEREDGE_SUB_RECIPROCATION_STATISTIC_AVG
  - A ---> B,C t_n
    D ---> A,E t_n+1
    X ---> A,D t_n+2
- reciprocation: DIR_HYPEREDGE_SUB_RECIPROCATION_STATISTIC_AVG
  - A ---> B,C t_n
    B ---> A,X t_n+1
- transitive tie: DIR_HYPEREDGE_CLOSURE_STATISTIC
  - A ---> B,C t_n
  
    B ---> D,E t_n+1
  
    A ---> D,X t_n+2
- cyclical tie: DIR_HYPEREDGE_CLOSURE_STATISTIC
  - A ---> B,C t_n
  
    B ---> D,E t_n+1
  
    D ---> A,X t_n+1
- triangle effect parents: DIR_HYPEREDGE_CLOSURE_STATISTIC
  - A ---> B,C t_n
  
    D ---> C,X t_n+1
  
    A ---> D,Y t_n+2
- triangle effect children: DIR_HYPEREDGE_CLOSURE_STATISTIC
  - A ---> B,C t_n
  
    A ---> D,E t_n+1

    C ---> D,X t_n+2
- hyperedge size: DIR_HYPEREDGE_SIZE_STATISTIC

## Regression models
sklearn.feature_selection.f_regression/r_regression to measure effect and significance of predictors 

## TODO:
- for china dataset, calculate percentage of cross-region nominations
