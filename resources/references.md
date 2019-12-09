# For future references

Since Github does not seem to support mermaid, typora screenshots have made thre way in this repository.  
Once mermaid is supported the following code are those used to generate the screenshots:

**<ins>Indus:</ins>**

```
graph TD
  subgraph External
    AA[OpenLDAP]
    AB[Github]
  end

  subgraph Industr
    BA[Host]
    BB[Jenkins]
    BC[staging]
    BD[production]

    subgraph staging_network
      BAA[TP]
      BAB[Redis]
    end

    subgraph production_network
      BBA[TP]
      BBB[Redis]
    end

  end

  BA --> |deploys|BB
  BA --> |deploys|BC
  BA --> |deploys|BD
  BB --> |authenticates with|AA
  BB --> |gets libraries from|AB
  
  BAA --> |connects to|BAB
  BBA --> |connects to|BBB
``` 

**<ins>CICD:</ins>**

``` 
graph TD
  A[Developer]
  
  subgraph CI/CD
    AA[Github]
    AB[Jenkins]
    AC[staging]
    AD[production]
  end

  A  --> |pushes to|AA

  AA --> |notifies|AB
  AB --> |deploys|AC
  AB --> |validates|AC
  AB --> |deploys|AD
```
