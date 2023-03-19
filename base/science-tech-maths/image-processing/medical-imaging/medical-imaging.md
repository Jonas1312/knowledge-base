# Medical Images

Many formats are used to store medical images. The most famous one is the DICOM standard, but we also find nifti, tiff, mhd, and many others.

## CT

Computed tomography (CT) scans, on the other hand, works much like an X-ray, only with greater, 3D detail of the organs, bones, and tissues inside your body.

A CT scanner is basically a rotating x-ray machine that takes sequential x-ray pictures of your body as it spins around.

During the scan, a narrow x-ray beam circles your body, taking a series of images from different angles. These images are stored in a computer that can, in turn, create a cross-sectional view of the body part under examination.

CT sinogram

The one downside to CT scans is the same issue that has plagued X-rays: they do use radiation, which means you cannot have multiple CT scans done in a short period of time without risk.

### Hounsfield units (HU)

a quantitative scale for describing radiodensity.

Hounsfield units are obtained from a linear transformation of the measured attenuation coefficients

The attenuation coefficient is a measure of how easily a material can be penetrated by an incident energy beam (e.g. ultrasound or x-rays). It quantifies how much the beam is weakened by the material it is passing through.

- radiodensity of air at STP = -1000 HU
- radiodensity of distilled water at standard temperature and pressure (STP) = 0 HU
- Soft tissue on contrast CT  +100 to +300
- +~2000 HU for very dense bone (cochlea)
- over 3000 for metals

### Slice thickness vs spacing

- Slice Thickness is determined by the detector width and pitch
- while reconstruction interval (=Spacing Between Slices) can be chosen arbitrarily

In conclusion to compute (safely!) the Spacing Between Slices (= Reconstruction Interval) use:

- Image Orientation (Patient)
- and Image Position (Patient)
- since they are available in either MR Image Storage or CT Image Storage instances.

## PET

PET scans (positron emission tomography scans)

PET scans use positrons. A tracer is injected into your body that allows the radiologist to see the area scanned.

Which modality would you use to evaluate glucose consumption by cancerous lesions? I am not sure, but I think PET imaging with SUVmax can help to quantify the glucose absorption.

It uses a special dye with radioactive tracers to help the machine capture changes in how the body’s working, such as how it absorbs sugar or how the brain’s functioning. These radioactive tracers are swallowed, inhaled, or injected into the veins,

The tracers collect in areas of the body with high chemical activity, which is typically a sign of disease such as cancer. The tracers are also used to measure blood flow, oxygen use, sugar levels, and the like.

## MRI

MRI scans (magnetic resonance imaging scans).

 MRI uses powerful magnets, radio waves, and computer technology to create its images

What is the typical main magnetic field strength of an MRI machine? The magnets in use today in MRI are in the 0.5-Tesla to 3.0-Tesla range, or 5,000 to 30,000 gauss.

## Differences

An MRI scan can be used when your organ shape or blood vessels are in question, whereas PET scans will be used to see your body’s function.

A PET scan is different from the other two imaging techniques because it’s mainly used to look at your organs rather than bones.

While PET scans do use radiation, they don’t use as much like X-rays or CT scans do, reducing the risk and allowing you to have multiple PET scans within a short amount of time without danger.

## Recognize CT vs MRI

- Can see the table? CT
- bones black? MRI. Bones have high HU in CT.
