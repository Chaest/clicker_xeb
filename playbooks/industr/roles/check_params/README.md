# Description

This role is used to check whether other roles needed paramaters were correctly set or not.  
It uses the `assert` module with the `quiet` parameter. Hence it requires a minimum ansible version of `2.8`.  
The assertions are quiet by default. This can be changed by setting the variable `verbose_assertions` to `true`.  

# Contributors

 - Emmanuel Pluot (Chaest@Github)
