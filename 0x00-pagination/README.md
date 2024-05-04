# 0x00. Pagination

`Back-end`
 - Weight: 1
 - Project will start May 2, 2024 4:00 AM, must end by May 7, 2024 4:00 AM
 - Checker was released at May 3, 2024 10:00 AM
 - An auto review will be launched at the deadline
  
![img](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/3646eb02de6527ca5d83.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240504%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240504T184258Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=985488d148f8a7705c92ab1cd95c96d5eb75f792ed8eba9859c4ed1d47b8fcf8)

## Resources

### Read or watch:

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your functions should have a documentation (python3 -c `'print(__import__("my_module").my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Setup: `Popular_Baby_Names.csv`

[use this data file](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240504%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240504T184733Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9d6d9c95edba3f906e248fe3c0cf90cbb6f93d027f39316a78d88dfdfa2ed169) for your project
