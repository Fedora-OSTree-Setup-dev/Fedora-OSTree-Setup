# Structure

The project has an structure of:

```
src
+-- interface
+-- misc
`-- utils
    +-- conf
    +-- core
    `-- shared
        +-- log
        `-- misc
```

`src/` contains the source code of the program, which is further broken down into:

1. `interface`, where the front-end related codes are stored, particularly
the commandline interface.

2. `misc` are where the not really important codes are stored such as type aliases.

3. `utils` where the functions that is called in `main.py` is stored, which is
further broken down into:

a. `conf` are everything related to the functions that deal with the config
file of the program.

b. `core` are the most crucial piece that executes each feature such as
removal of applications as well as installation.

c. `shared` are where the self written modules called by different modules in
`core` are stored, this is further broken down into:

1. `log`, the logging system.

2. `misc`, are another not really important codes, although plays a
crucial role.
