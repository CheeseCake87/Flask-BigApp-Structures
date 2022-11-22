# How to contribute to the project

There are two folders that your structure should be in:
`app/blueprints` and `app/structures`.

#### Your structure name must be unique. Check the structures folder of this project to make sure your structure name is not already taken.

The blueprint that showcases your structure should be the name of your structure
followed by `_example`. For example, if your structure is called `my_structure`,
then your blueprint should be called `my_structure_example`. 

The structure itself should be in the `app/structures` folder.

An example folder structure would be:
```
app/
├── blueprints/
│   └── my_structure_example/
│       ├── routes/...
│       ├── static/...
│       ├── templates/
│           └── my_structure_example/...
│       ├── __init__.py
│       └── config.py

...

├── structures/
│   └── my_structure/
│       ├── static/...
│       └── templates/...
│           └── my_structure/...
│       └── LICENSE
```

Please include your license in the root of your structure folder.

You can create a pull request to add your structure to the project, 
or email a link of your project files to: `flask-bigapp@uilix.com`
#### Note: Emails that contain zip files will be ignored and deleted.