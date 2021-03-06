# crpropa_singularity

Recipe to build [Singularity](https://sylabs.io/guides/latest/user-guide/introduction.html) image containing [CRPropa](https://github.com/CRPropa/CRPropa3) - Cosmic Ray Propagation Framework.

## use container

Prebuilt container is available in "releases".

( app.py is your python script using crpropa )

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

### get singularity at ubuntu

this guide, https://github.com/sylabs/singularity/blob/master/INSTALL.md, works pretty well on recent ubuntu (21.10).

### other notes

Container is based on Rocky Linux docker image.


