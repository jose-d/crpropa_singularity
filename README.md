# CRPropa Apptainer Image

This repository contains a recipe to build an [Apptainer](https://apptainer.org/user-guide/introduction.html) image for [CRPropa](https://github.com/CRPropa/CRPropa3) - the Cosmic Ray Propagation Framework.

## Using the Container

A prebuilt container is available in the "releases" section.

To run our example Python app (`example.py`), use the following command:

```bash
apptainer exec crpropa.sif python ./example.py
CosmicRay at z = 0
  source:  Particle 1000010010, E = 200 EeV, x = 100 0 0 Mpc, p = -1 0 0
  current: Particle 1000010010, E = 0.998292 EeV, x = -13173.3 0 0 Mpc, p = -1 0 0
Propagated distance 13273.263588242868 Mpc
```

## Advanced: Creating the Container

### Create SIF File

To build the SIF file for production, run:

```bash
sudo apptainer build ./Apptainer.sif ./crpropa.def
```

### Development: Build in Sandbox

To build the container in a sandbox environment for development, run:

```bash
apptainer build --fakeroot --sandbox sandbox ./crpropa.def
```

## Technical Information

### Installing Apptainer on Ubuntu

Follow the [installation guide](https://apptainer.org/docs/admin/main/installation.html) for Apptainer, which works well on recent Ubuntu versions (24.04).

## Additional Notes

The container is currently based on the Rocky Linux 9 Docker image.
