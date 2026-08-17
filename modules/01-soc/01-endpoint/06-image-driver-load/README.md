# Image and Driver Load Activity

**Path:** `modules/01-soc/01-endpoint/06-image-driver-load`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.1.6.1 | K | Image and driver load activity concepts | 1.1.6 a–d | A / B / C | A / B / B | A / A / A |
| 1.1.6.2 | T | Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred | 1.1.6.1 task 1 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.6.3 | T | Create a SIEM query to detect specific image or driver load activity | 1.1.6.1 task 2 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

The teaching-unit ID is **1.1.6**. Registry is **1.1.5**. Zeek is **1.2**. File create is **1.1.3**. Persistence / BYOVD is **2.6**. Not Sysmon install. No lab.

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
- `assets/` — empty
