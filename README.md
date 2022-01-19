# create container

## create sif file

```sudo singularity build ./Singularity.sif ./crpropa.def```


## build in sandbox

```singularity build --fakeroot --sandbox sandbox ./crpropa.def```
