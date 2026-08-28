# Module 1.1.3 – File System Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C ; 1.1.3.2 2b / 3c / 4c ; 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B ; 1.1.3.2 1a / 2b / 3c ; 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A ; 1.1.3.2 1a / 1a / 1a ; 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a file event: create / rename-move / delete / modify / read, path, hash, and who touched the file.
2. Describe what a Sysmon or MDE file event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.3.1 – File system activity concepts
- T: 1.1.3.2 – Analyze a file event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific file operations

---

## 1. Key Concepts

SOC analysts read **file** events on a host to see what happened to a file, where, and by which process. That is daily alert work: an alert names a host, and you have to say whether a file was created, renamed or moved, deleted, changed, or read — from which path, and by whom. **1.1.1** named the five kinds of host activity. This lesson is the **file** kind. It is **not** Zeek (`files` / `conn`) (**1.2**). It is **not** how to install Sysmon. It is **not** a process-create write-up (**1.1.2**).

**File system activity** is endpoint telemetry about a file: it was **created**, **renamed or moved**, **deleted**, **modified**, or **read** (where that action is logged). In a SIEM, that event usually shows up as a row in a file table.

| Idea | What to read |
|------|----------------|
| **Create / rename-move / delete / modify / read** | Create = a file appeared. Rename-move = same object, new name or folder. Delete = it is gone. Modify / read = where logged. |
| **Path, name, extension** | Sysmon `TargetFilename`; MDE `FolderPath` + `FileName`. Path is where. Name and extension can lie (`invoice.pdf.exe`). |
| **Hashes** | SHA256 when the event carries it. Empty ≠ clean. Sysmon **11** often has no hash. |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. Who did this **to the file**. Not a process-create parent-child write-up (**1.1.2**). |

**How this shows up:** Sysmon **11** (create), **23** (delete, archived), **26** (delete detected); MDE `DeviceFileEvents` (`ActionType`, `FolderPath`, `FileName`, SHA256, `InitiatingProcess*`). Same activity, different field names.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **FileCreated** | A file appeared or was overwritten | Event **11** |
| **FileRenamed** | Same object, new name or folder | Not 11 / 23 / 26 |
| **FileDeleted** | The file is gone | Event **23** / **26** |
| **FileModified** | Content changed — where logged | Not 11 / 23 / 26 |

The full set is in the Defender portal schema. Do not invent a value. **Read** is where that action is logged. Do not assume a `FileRead` event in `DeviceFileEvents`. If your Sysmon feed is only 11 / 23 / 26, rename / modify / read will not be there. Write “not logged,” not “did not happen.”

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what happened to which file, by whom. Create, rename-move, delete, modify, or read. Do not jump to a process create (**1.1.2**) or Zeek (**1.2**).
- Given: Sysmon **11**, `Image` `wscript.exe`, `TargetFilename` Temp `update.exe`, no hash. **What occurred:** script host created `update.exe` under Temp. Hash not logged. The process create of `wscript` is a different event.
- Query: names a **specific** pattern (initiator + path + extension), not “all file events.”

Host-network, registry, and image-load events are the next **1.1** lessons.

---

## 2. Knowledge Check

1. Sysmon Event 11 is a rename. True or false?
2. `wscript.exe` creates Temp `update.exe` (Sysmon 11, no hash). In one sentence, what occurred?
3. A SIEM query that matches every file event is a good “specific file operation” query. True or false?

---

## 3. Summary

A file event tells you what happened to which file, by whom. Path and initiator are what you trust. A missing hash is a gap. A query names a specific pattern.

**Next:** **1.1.4** Network activity (endpoint).

---

## 4. Related modules

- 1.1.2 – Process activity
- 1.1.4 – Network activity (endpoint)
- 1.1.5 – Registry activity
- 1.2 – Zeek
