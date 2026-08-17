# Image and Driver Load Activity

**Path:** `modules/01-soc/01-endpoint/06-image-driver-load`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.6.1 | K | Image and driver load activity concepts | 1.1.6 a–d |
| 1.1.6.2 | T | Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred | 1.1.6.1 task 1 |
| 1.1.6.3 | T | Create a SIEM query to detect specific image or driver load activity | 1.1.6.1 task 2 |

The teaching-unit ID is **1.1.6**. Process activity is **1.1.2**. File system activity is **1.1.3**. Host-observed network is **1.1.4**. Registry is **1.1.5**. This lesson does not teach Sysmon install or config. Persistence / BYOVD hunt methodology is **2.6**.

## Concepts taught

- image and driver load activity
- user-mode image load vs kernel driver load
- path, hashes, signed vs unsigned
- initiating process (image load)
- Sysmon 6 / 7 and DeviceImageLoadEvents

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)
