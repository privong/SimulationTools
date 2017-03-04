# Identikit Quickstart

This assumes you have successfully compiled and installed zeno and Identikit and the executables are somewhere in your $PATH.

## Creating an Initial Library

To make the test particle simulations, you'll need to run something like the following commands:

```
$ mkdir r121; make -f InitialData r121/i121.dat
...
$ make -f InitialData jhat12X.dat
...
```

The first line will create a zeno initial conditions snapshot for an equal mass, eccentricity=1 pass where the pericenter approach is 1/16 length units.

The second command creates the file with the information on the initial angular momentum for all the test particles. It is used to tell Identikit which particles to display. This jhat file is valid for the simulations beginning with "r12".

To run the simulation and create the test particle library, add the following text to another makefile (which I call "Run"):

```
run121:
   treecode in=r121/i121.dat out=r121/r121_%04x.dat \
       save=r121/r121.state%01d dtime=1/256 eps=0.0075 \
       usequad=t tstop=10 dtout=1/16
```

You can then evolve the system by running the following command:

```
$ make -f Run run121
```

To do this for other pericenter approach distances, re-run the above make command for the InitialData file, substituting other codes. The rXYZ code corresponds to:

* X - orbital eccentricity (always 1 for the provided sims)
* Y - for mass ratio of a:b, Y=a+b. For equal mass encounters, Y=2
* Z - pericentric separation in 16ths of a length unit. Z=3 has a pericentric separation of 3/16 length units.

## Exploring Encounters in Identikit

*This section is written primarily for the [Identikit 1](http://adsabs.harvard.edu/abs/2009AJ....137.3071B) technique of manually searching parameter space for models.
However, the image projection information is valid for both Identikit 1 and [Identikit 2](http://adsabs.harvard.edu/abs/2011MNRAS.413.2860B).*

Once you've created as many models as you feel is necessary, you can run Identikit using something like the following:

```
$ idkit jhat=jhat12X.dat sims=r124/r124_%04x.dat,r125/r125_%04x.dat
```

This will load Identikit and give the program access to the simulations with equal-mass encounters and pericentric separations of 4/16 and 5/16 length units.

To explore the parameter space, use the three mouse buttons (you'll need a 3-button mouse) and keyboard commands (press '?' inside Identikit to see the commands).

By default, identikit loads such that the left mouse button controls the viewing angles, and the other two mouse buttons control the orientations of disk 1 and 2. Spacebar (backspace) moves forwards (backwards) in time.  'n' ('p') move ahead (behind) in the comma delineated list of simulations provided when Identikit was invoked. Other keys modify the mouse behavior to allow you to explore other regions of parameter space (see '?' above). The values for some parameters are shown in the lower-right panel.

I would recommend playing around with the interface a bit before trying to load in data cube projections. That way you can start to get a feel for how changing the parameters in real-time

Regarding the data cube, you'll want to create a sky-plane (XY) and two position velocity (XV and VY) images by projecting the data cubes along the appropriate axes. It's a bit up to you how you want to do that, but there are some important details on the ppm images to give to identikit:
- they must have the same pixel dimensions
- the spatial axes in all projections must be the same size (i.e., they must be the same number of arcsec on a side)

These images can be passed to Identikit via the xyimage, xvimage, and vyimage arguments. These will then be displayed in the appropriate panels. Note the images must be in ppm format.

The direction of increasing velocity is important. In the XV panel (lower-left), velocity should increase towards the top and in the VY panel (upper-right) velocity should increase towards the right.

Good luck!
