# masterarbeit

## Notes:
- in bucharest dataset, the event dataset contains all contact nominations. The patient dataset contains all
patients who have been recorded as positive. All referees from the event dataset are contained in the patient dataset.
However, only some referrals are contained in the patient dataset, and not all patients are also recorded as referees.
    - referees ⊆ patients
    - referrals = A ∪ B; A ⊆ patients, B ⊄ patients
    - patients = referees ∪ A ∪ C; C ⊅ referees, C ⊅ referrals

- REM node attribute covariates can be source-level, target-level, and source-target-relation level
- RHEM node attribute covariates can either be source-receiver set relation level
## Questions for next meeting:
- how to include relational node attribute covariates in REM analysis?

### REM Covariates:
#### Note attributes:
- age difference
- sex difference
- residency difference (where applicable)
- job difference (where applicable)
- more from big china dataset

#### Network effects
- repetition:
  - A ---> B t_n
  
    A ---> B t_n+1
  - A ---> B t_n
    
    A ---> X t_n+1
- reciprocity:
  - A ---> B t_n
    
    A <--- B t_n+1
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

## TODO:
