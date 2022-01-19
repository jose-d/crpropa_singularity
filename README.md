# crpropa_singularity

Recipe to build [Singularity](https://sylabs.io/guides/latest/user-guide/introduction.html) image containing [CRPropa]() - Cosmic Ray Propagation Framework.
Prebuilt container is available in "releases".

## use container

( app.py is python script importing and using crpropa )

```
-bash-4.2$ ./Singularity.sif python3 app.py 
Python version
3.6.8 (default, Nov  9 2021, 14:44:26) 
[GCC 8.5.0 20210514 (Red Hat 8.5.0-3)]
we can import crpropa, cool.
-bash-4.2$
```

## create container

### create sif file (production)

```sudo singularity build ./Singularity.sif ./crpropa.def```

### build in sandbox (development)

```singularity build --fakeroot --sandbox sandbox ./crpropa.def```

## tech stuff

Container is based on Rocky Linux docker image.
