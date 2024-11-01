# crpropa_singularity

# CRPropa Apptainer Image

This repository contains a recipe to build an [Apptainer](https://apptainer.org/user-guide/introduction.html) image for [CRPropa](https://github.com/CRPropa/CRPropa3) - the Cosmic Ray Propagation Framework.

## Using the Container

A prebuilt container is available in the "releases" section.

To run your Python script (`app.py`) using CRPropa, use the following command:

```bash
./Apptainer.sif python3 app.py
```

Example output:

```bash
Python version
3.6.8 (default, Nov  9 2021, 14:44:26) 
[GCC 8.5.0 20210514 (Red Hat 8.5.0-3)]
we can import crpropa, cool.
```

## Creating the Container

### Production: Create SIF File

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

### Additional Notes

The container is based on the Rocky Linux 9 Docker image.
