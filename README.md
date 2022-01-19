# crpropa_singularity

Recipe to build [Singularity](https://sylabs.io/guides/latest/user-guide/introduction.html) image containing [CRPropa]() - Cosmic Ray Propagation Framework.


## create container

### create sif file (production)

```sudo singularity build ./Singularity.sif ./crpropa.def```

### build in sandbox (development)

```singularity build --fakeroot --sandbox sandbox ./crpropa.def```
