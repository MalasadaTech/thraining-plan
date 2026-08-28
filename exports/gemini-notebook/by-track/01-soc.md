# Track 1 — SOC

This is classroom fiction, not live org policy. If a lesson and the story bible disagree, **the bible wins**. Night Owl / Harbor in a lesson means **Pink River Dolphin (PRD)** / **Dixon, Yamada, & Associates (DYA)**.

---

# Lesson 1.1.1 – Endpoint activity (the map)

Source: `modules/01-soc/01-endpoint/01-endpoint-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the five kinds of **host activity** this unit will teach.
2. Given a one-line description, say whether it is **process**, **file**, **registry**, **host-network**, or **image/driver load**.

**Mapped Proficiency Items:**
- K: 1.1.1.1 – Endpoint activity (the map)
- T: 1.1.1.2 – Given a one-line description, name the activity type

---

## 1. Key Concepts

An alert usually names a **host** — a laptop, server, or other device. Something on that host generated a log. Before you describe what happened, you have to know **what kind of activity** the log is about. That is the job in this lesson: name the kind first, so you do not mix process, file, and network details into one write-up.

A host generates **logs** when something happens on it. Each log is one **event**. In a SIEM, that event usually shows up as a **row** in a table. Later lessons may still say “row.” Here it means the same thing as the log.

| Kind | What happened |
|------|----------------|
| **Process** | A program ran, ended, or touched another program |
| **File** | A file was created, moved, changed, read, or deleted |
| **Registry** | A key or value was set, deleted, or renamed |
| **Host-network** | This host talked (IP, port, domain) — the *process* started it |
| **Image / driver load** | A DLL or driver was loaded |

**Host-network** means the *host* logged that this device talked. It is not a Zeek lesson. Zeek watches the wire and does not name the process that opened the socket.

**Sysmon** and **MDE** (Microsoft Defender for Endpoint) are two tools that record those **same** five kinds of activity. They use different field names. They are not two different sets of facts. This course uses both as examples. This is **not** how to install Sysmon.

You will learn **one activity type at a time** after this lesson. This lesson only names the five kinds. The next lessons each cover one kind in detail.

This is **endpoint** telemetry: logs from the host itself. Protocol deep-dive is Zeek (**1.2**).

**What good looks like:** someone gives you one line. You name the kind. You do not describe fields yet.

- Given: “A program started on the host.” **Process.**
- Given: “A file appeared in Temp.” **File.**
- Given: “This host connected to an IP and port.” **Host-network.**

Do not tell the rest of the incident. Do not try to read process fields yet (**1.1.2**).

---

## 2. Knowledge Check

1. Sysmon and MDE are two different stories. True or false?
2. “A program started on the host.” Which activity type is that?
3. “This host connected to an IP and port.” Process, or host-network?

---

## 3. Summary

There are five kinds of host activity. Sysmon and MDE record the same kinds with different field names. Name the kind before you describe the event. Zeek is later.

**Next:** **1.1.2** Process activity.

---

## 4. Related modules

- 0.1 – How this course is laid out
- 1.1.2 – Process activity
- 1.2 – Zeek

---

# Lesson 1.1.2 – Process Activity

Source: `modules/01-soc/01-endpoint/02-process-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C ; 1.1.2.2 2b / 3c / 4c ; 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B ; 1.1.2.2 1a / 2b / 3c ; 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A ; 1.1.2.2 1a / 1a / 1a ; 1.1.2.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a process event: create / terminate, parent-child, command line, user, hashes, and process access.
2. Describe what a Sysmon or MDE process event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.2.1 – Process activity concepts
- T: 1.1.2.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.2.3 – Create a SIEM query to detect specific process activity

---

## 1. Key Concepts

SOC analysts read **process** events on a host to see who ran what. That is daily alert work: an alert names a host, and you have to say which program started, ended, or touched another — from whom, and as whom. **1.1.1** named the five kinds of host activity. This lesson is the **process** kind. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Process activity** is endpoint telemetry about a running program: it **started**, it **ended**, or one process **touched** another. In a SIEM, that event usually shows up as a row in a process table.

| Idea | What to read |
|------|----------------|
| **Create / terminate** | Sysmon **1** / **5**. MDE create is `ActionType` **ProcessCreated**. Terminate is Sysmon 5 — do not assume `ProcessTerminated` on this table. |
| **PID, name, command line** | `ProcessId`, image/name, `CommandLine` / `ProcessCommandLine`. The image name can be fake. The command line is often what actually ran. |
| **Parent-child** | PPID, parent name, parent command line; MDE `InitiatingProcess*` |
| **Integrity / user** | Integrity level; `User` / account (where logged). Empty is a gap, not “not admin.” |
| **Hash / original filename** | SHA256; `OriginalFileName` (PE resource — can disagree with the on-disk name) |
| **Process access** | Sysmon **10**: source → target (who touched whom). Not a create. |

**How this shows up:** Sysmon **1** / **5** / **10**; MDE `DeviceProcessEvents` (`ActionType`, `InitiatingProcess*`, `ProcessCommandLine`, SHA256). On MDE, the **initiating** process is the parent. Same activity, different field names.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ProcessCreated** | A process launched | Event **1** |
| **OpenProcess** | A process opened a handle to another (who touched whom) | Event **10** |

The full set is in the Defender portal schema. Do not invent a value. **Terminate** is Sysmon **5**. Do not assume a `ProcessTerminated` event in `DeviceProcessEvents`.

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — who ran what, from whom, as whom. Create, terminate, or access. Do not jump to file, DNS, or registry (**1.1.3**–**1.1.5**).
- Given: `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …` as `jlee`. **What occurred:** script host launched hidden encoded PowerShell. The hash of `powershell.exe` can still be fine. The parent and command line are what you write down.
- Query: names a **specific** pattern (parent + command-line fragment), not “all processes.”

File, host-network, registry, and image-load events are the next **1.1** lessons.

---

## 2. Knowledge Check

1. Sysmon Event 10 is a process start. True or false?
2. `wscript.exe` (Temp `.vbs`) creates `powershell.exe -enc …`. In one sentence, what occurred?
3. A SIEM query that matches every process is a good “specific process activity” query. True or false?

---

## 3. Summary

A process event tells you who ran what, from whom, as whom. That is a create, a terminate, or an access. Command line and parent are what you trust. A query names a specific pattern.

**Next:** **1.1.3** File system activity.

---

## 4. Related modules

- 1.1.1 – Endpoint activity (the map)
- 1.1.3 – File system activity
- 1.1.4 – Network activity (endpoint)
- 1.2 – Zeek

---

# Lesson 1.1.3 – File System Activity

Source: `modules/01-soc/01-endpoint/03-file-system-activity/student-guide.md`

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

---

# Lesson 1.1.4 – Network Activity (Endpoint)

Source: `modules/01-soc/01-endpoint/04-network-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a host-network event: IP/port, protocol, direction, domain/URL when logged, and which process talked.
2. Describe what a Sysmon or MDE endpoint network event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.4.1 – Network activity (endpoint) concepts
- T: 1.1.4.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific endpoint network activity

---

## 1. Key Concepts

SOC analysts read **host-network** events on a host to see which process on this device talked, and to where. That is daily alert work: an alert names a host, and you have to say who opened the socket — to which IP and port, or which name. **1.1.1** named the five kinds of host activity. This lesson is the **host-network** kind. The point of this lesson versus Zeek is the **initiating process**. Zeek watches the wire and does not name the process that opened the socket. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Network activity (endpoint)** is host telemetry that a process **connected** (or tried to) or issued a **DNS query** (when that is logged here). In a SIEM, that event usually shows up as a row in a network table.

| Idea | What to read |
|------|----------------|
| **Source / dest IP and port, protocol, direction** | Sysmon `Source*` / `Destination*`, `Protocol`, `Initiated`. MDE `Local*` / `Remote*`, `Protocol`. `Initiated=true` = this process started the connection. |
| **Domain / URL when logged** | Sysmon 3 `DestinationHostname`; Sysmon **22** `QueryName` if 22 is in the feed; MDE `RemoteUrl`. Empty ≠ “no DNS happened.” |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. **Who talked.** A Zeek `conn` log will not give you this field. |

**How this shows up:** Sysmon **3** (connect) and **22** (DNS, if logged here); MDE `DeviceNetworkEvents` (`ActionType`, `InitiatingProcess*`, `RemoteUrl`, `Local*` / `Remote*`). Same activity, different field names. This is **host-observed** activity. Protocol deep-dive is **1.2**.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ConnectionSuccess** | This process completed a connection | Event **3** (`Initiated` tells direction) |

The full set is in the Defender portal schema. Do not invent a value. **DNS** on the endpoint is Sysmon **22** when that event is in the feed. If Event **22** is not in the Sysmon feed, write “DNS not logged on the endpoint,” not “no DNS happened.”

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — which process talked, to which IP/port (or which name), which direction. Do not jump to a process create (**1.1.2**), a file drop (**1.1.3**), or a Zeek `conn` / `dns` field (**1.2**).
- Given: MDE `ConnectionSuccess`, `powershell.exe -enc …` → `203.0.113.88:443`, `RemoteUrl` empty. **What occurred:** hidden encoded PowerShell successfully connected outbound TCP/443 to that IP. URL not logged. The process create is a different event.
- Query: names a **specific** pattern (initiator + dest port or remote IP), not “all connections.”

Registry and image-load events are the next **1.1** lessons.

---

## 2. Knowledge Check

1. A Zeek `conn` log names the initiating process. True or false?
2. `powershell.exe -enc …` has `ConnectionSuccess` to `203.0.113.88:443` and no `RemoteUrl`. In one sentence, what occurred?
3. A SIEM query that matches every endpoint network event is a good “specific endpoint network activity” query. True or false?

---

## 3. Summary

A host-network event tells you which process talked, and to where. Direction and initiator tell the story. A missing name is a gap. Zeek does not name the process. A query names a specific pattern.

**Next:** **1.1.5** Registry activity.

---

## 4. Related modules

- 1.1.3 – File system activity
- 1.1.5 – Registry activity
- 1.1.2 – Process activity
- 1.2 – Zeek

---

# Lesson 1.1.5 – Registry Activity

Source: `modules/01-soc/01-endpoint/05-registry-activity/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.5.1 A / B / C ; 1.1.5.2 2b / 3c / 4c ; 1.1.5.3 2b / 3c / 4c  
- Hunter: 1.1.5.1 A / B / B ; 1.1.5.2 1a / 2b / 3c ; 1.1.5.3 1a / 2b / 3c  
- CTI: 1.1.5.1 A / A / A ; 1.1.5.2 1a / 1a / 1a ; 1.1.5.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a registry event: hive, key → value, set / delete / rename, and who changed it.
2. Describe what a Sysmon or MDE registry event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.5.1 – Registry activity concepts
- T: 1.1.5.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.5.3 – Create a SIEM query to detect specific registry operations

---

## 1. Key Concepts

SOC analysts read **registry** events on a host to see what changed in a key or value, and which process changed it. That is daily alert work: an alert names a host, and you have to say which hive and key were set, deleted, or renamed — and by whom. **1.1.1** named the five kinds of host activity. This lesson is the **registry** kind. It is **not** a persistence catalog (**3.6**). It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Registry activity** is endpoint telemetry about a **key or value** that was **set**, **deleted**, or **renamed**. In a SIEM, that event usually shows up as a row in a registry table.

| Idea | What to read |
|------|----------------|
| **Hive and key → value** | Hive (`HKLM` / `HKCU`, or `\REGISTRY\MACHINE\` / `\REGISTRY\USER\`). The **key** is the path. The **value** is the named slot plus **data**. Sysmon often writes `HKU\<SID>` for the user hive — that is the same tree as HKCU. |
| **Set / delete / rename** | Set = something was written. Delete = it is gone. Rename = same object, new name. |
| **Example locations** | Run / RunOnce; `...\Services\<name>`. Places you will see. Not a persistence catalog (**3.6**). |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. Who changed the key. Not a process-create write-up (**1.1.2**). |

**How this shows up:** Sysmon **12** (create/delete key or value), **13** (SetValue), **14** (rename); MDE `DeviceRegistryEvents` (`ActionType`, `RegistryKey`, `RegistryValueName`, `RegistryValueData`, `InitiatingProcess*`). Same activity, different field names.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **RegistryValueSet** | Data was written to a named value | Event **13** |
| **RegistryKeyCreated** | A key appeared | Event **12** |
| **RegistryKeyDeleted** / **RegistryValueDeleted** | The key or value is gone | Event **12** |
| **RegistryKeyRenamed** | Same key, new name | Event **14** |

The full set is in the Defender portal schema. Do not invent a value. Sysmon **14** also logs value rename. Do not assume an MDE `RegistryValueRenamed` ActionType on this table.

If value data is empty, write “data not logged,” not “empty on purpose.” If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what happened to which key/value, by whom. Set, delete, or rename. Name Run or Services as a **location** if that is where it sat. Do not deliver a persistence hunt (**3.6**).
- Given: Sysmon **13**, `powershell.exe`, `\REGISTRY\USER\…\Run\Updater` = Temp `update.exe`. **What occurred:** PowerShell set HKCU Run value `Updater` to that Temp path. The file create of `update.exe` is a different event (**1.1.3**).
- Query: names a **specific** pattern (initiator + key path), not “all registry events.”

Image and driver load is the last **1.1** child.

---

## 2. Knowledge Check

1. A Run-key event is a finished persistence hunt. True or false?
2. `powershell.exe` SetValue on HKCU `Run\Updater` = Temp `update.exe`. In one sentence, what occurred?
3. A SIEM query that matches every registry event is a good “specific registry operation” query. True or false?

---

## 3. Summary

A registry event tells you what changed in the hive, by whom. That is a set, a delete, or a rename. Key, value, and initiator are what you write down. Run and Services are locations, not a hunt course. A query names a specific pattern.

**Next:** **1.1.6** Image and driver load.

---

## 4. Related modules

- 1.1.1 – Endpoint activity (the map)
- 1.1.3 – File system activity
- 1.1.4 – Network activity (endpoint)
- 1.1.6 – Image and driver load
- 1.2 – Zeek
- 3.6.1 – Persistence techniques (later)

---

# Lesson 1.1.6 – Image and Driver Load Activity

Source: `modules/01-soc/01-endpoint/06-image-driver-load/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C ; 1.1.6.2 2b / 3c / 4c ; 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B ; 1.1.6.2 1a / 2b / 3c ; 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A ; 1.1.6.2 1a / 1a / 1a ; 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read an image or driver load event: user-mode image vs kernel driver, path, hash, signed vs unsigned (where logged), and who loaded it.
2. Describe what a Sysmon or MDE image or driver load event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

---

## 1. Key Concepts

SOC analysts read **image and driver load** events on a host to see that a module entered a process, or that a driver entered the kernel. That is daily alert work: an alert names a host, and you have to say what was loaded, into whom (or into the kernel), from where, and whether it was signed if that is logged. **1.1.1** named the five kinds of host activity. This lesson is the **image / driver load** kind. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Image and driver load activity** is endpoint telemetry that a **user-mode image** (usually a DLL) was mapped into a process, or that a **kernel driver** was loaded. In a SIEM, that event usually shows up as a row in a table.

| Idea | What to read |
|------|----------------|
| **User-mode vs kernel** | User-mode = a process loaded a module (Sysmon **7** / MDE). Kernel = a driver entered the kernel (Sysmon **6**). Not a process start. |
| **Path, hashes, signed vs unsigned** | Path is where it loaded from (Sysmon `ImageLoaded`; MDE `FolderPath` + `FileName`). Hashes of the loaded bytes when present (SHA256; MDE often carries SHA1 instead). `Signed` / signature fields **where logged**. Empty is a gap, not “unsigned.” |
| **Initiating process** | Sysmon 7 `Image` is the process; `ImageLoaded` is the module. MDE `InitiatingProcess*` is the process that loaded the module. Event **6** is kernel-wide — it has no user-mode parent field. Do not invent one. |

**How this shows up:** Sysmon **6** (driver) / **7** (image load); MDE `DeviceImageLoadEvents`. Same activity, different field names. Event **7** is noisy and often sampled or off. If you have no 7 / no `DeviceImageLoadEvents`, write “image load not logged.” Do not invent a load from a file-create event (**1.1.3**).

MDE `ActionType` on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ImageLoaded** | A process loaded a module | Event **7** |

`DeviceImageLoadEvents` is DLL load activity. Driver load on the endpoint is Sysmon **6**. Do not treat a `.sys` path on this MDE table as a kernel driver load, and do not invent a driver `ActionType` here. The full set is in the Defender portal schema.

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what was loaded, into whom (or into the kernel), from where, signed or not if logged. Do not jump to a file create (**1.1.3**) or a persistence / BYOVD write-up.
- Given: Sysmon **7**, `Image` `powershell.exe`, `ImageLoaded` Temp `update.dll`, `Signed=false`. **What occurred:** PowerShell loaded an unsigned DLL from Temp. The file create of that DLL, if you have one, is a different event.
- Query: names a **specific** pattern (process + path, or Event **6** + driver path), not every image or driver load.

This is the last **1.1** host-activity lesson. Protocol deep-dive is **1.2**.

---

## 2. Knowledge Check

1. Sysmon Event 6 is a DLL load into a process. True or false?
2. `powershell.exe` loads Temp `update.dll` (`Signed=false`). In one sentence, what occurred?
3. A SIEM query that matches every image or driver load event is a good “specific image or driver load” query. True or false?

---

## 3. Summary

An image or driver load event is a module entering a process, or a driver entering the kernel. Path and initiator tell the story. Signed empty is a gap. A file create is not a load. A query names a specific pattern.

**Next:** **1.2.1** Zeek concepts.

---

## 4. Related modules

- 1.1.1 – Endpoint activity (the map)
- 1.1.5 – Registry activity
- 1.1.3 – File system activity
- 1.2.1 – Zeek concepts

---

# Lesson 1.2.1 – Zeek Concepts

Source: `modules/01-soc/02-zeek/01-concepts/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.1.1 A / B / C  
- Hunter: 1.2.1.1 B / C / C  
- CTI: 1.2.1.1 A / B / B  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what Zeek is, and what an engine does.
2. Say why you pull PCAP when you already have a Zeek log.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

---

## 1. Key Concepts

An alert can name traffic on the **wire**, not only a host. A network sensor generated a log. Before you describe that traffic, you have to know what **Zeek** is: a framework that watched the wire and wrote structured fields. That is the job in this lesson: say what Zeek is, what an engine does, and why you still pull PCAP.

**1.1** was host and endpoint activity — logs from the host. This unit is **network-sensor** telemetry. Zeek watches the wire and writes structured logs. It does **not** name the initiating process. That field is host-network activity (**1.1.4**).

**Zeek** is a network analysis framework. It is not primarily a signature IDS. It classifies traffic and writes logs you query in a SIEM.

**Engines** (scripts / analyzers) look at a flow, decide what protocol it is, and **extract** the fields for that protocol. That is how applications and protocols **surface** (show up) as logs you can query. Conn, DNS, TLS, HTTP, SMTP, files, and weird are later lessons. This lesson is only that they exist and that they surface applications and protocols as logs.

**PCAP** is a packet capture — the usual next artifact. A Zeek log is an **extract**: the fields an engine already wrote. You pull PCAP to **verify** that extract, or to **expand** what the log does not carry. This is not a PCAP analysis course. This lesson does not teach Wireshark or the site download path.

**What good looks like:** you can say Zeek is the sensor log, an engine extracted the protocol, and PCAP is how you check or fill a gap. You do not open `conn` fields yet (**1.2.2**).

---

## 2. Knowledge Check

1. Zeek is primarily a signature-based IDS. True or false?
2. What does an engine do?
3. You already have a Zeek log. Why pull PCAP?

---

## 3. Summary

Zeek writes structured logs from the wire. Engines extract protocol. PCAP verifies or expands the extract. The process name is on the host log, not here.

**Next:** **1.2.2** Conn engine.

---

## 4. Related modules

- 1.1.6 – Image and driver load (previous)
- 1.1.4 – Network activity (endpoint)
- 1.2.2 – Conn engine

---

# Lesson 1.2.2 – Conn Engine

Source: `modules/01-soc/02-zeek/02-conn-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.2.1 A / B / C ; 1.2.2.2 2b / 3c / 4c ; 1.2.2.3 2b / 3c / 4c  
- Hunter: 1.2.2.1 B / C / C ; 1.2.2.2 3c / 4c / 4c ; 1.2.2.3 3c / 4c / 4c  
- CTI: 1.2.2.1 A / A / B ; 1.2.2.2 1a / 1a / 2b ; 1.2.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `conn` event: originator and responder IP and port, and how the connection ended.
2. Describe what a `conn` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`conn`** log to see who talked to whom on the **wire**, and how the connection ended. That is daily alert work: an alert names an IP or a connection, and you have to say which address started the talk, which address was contacted, on which ports, and whether the attempt completed, sat unanswered, or was refused. **1.2.1** taught that Zeek engines extract protocol data from the wire. This lesson is the **`conn`** extract. It does **not** name the initiating process. That is host-network telemetry (**1.1.4**).

The **`conn`** log is one **event** per connection Zeek saw. In a SIEM, that event usually shows up as a **row** in a table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Source IP** | `id.orig_h` — **originator** IP. Who started the talk from Zeek’s view. Not automatically an internal host. |
| **Source port** | `id.orig_p` — originator port |
| **Destination IP** | `id.resp_h` — **responder** IP. Who was contacted. |
| **Destination port** | `id.resp_p` — responder port |
| **Connection state / history** | `conn_state` / `history`. How it ended, and a short flag string of what was seen (`S` SYN, `H` SYN-ACK, `F` FIN, `R` RST) |

**States you will use:** **`SF`** = established and torn down cleanly. **`S0`** = attempt, no reply. **`REJ`** = attempt refused. If you see another state, say what the field shows. Do not invent a story the flags do not support.

`id.orig_h` is the originator, not the destination. Originator is not a synonym for “our network.” Zeek labels the side that started the talk, wherever that address lives.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open DNS or TLS fields yet.

**What good looks like:**

- Describe: one sentence — originator IP/port → responder IP/port, state. Do not name a process. Do not call it C2 from port 443 alone.
- Given: `id.orig_h` a workstation, `id.resp_h` `203.0.113.88`, `id.resp_p` `443`, `conn_state` `SF`. **What occurred:** that host completed a TCP connection to `203.0.113.88:443`. Who launched the socket is on the **host** (**1.1.4**).
- Query: names a **specific** pattern (responder IP or port + state), not every connection.

DNS fields are the next Zeek lesson (**1.2.3**).

---

## 2. Knowledge Check

1. `id.orig_h` is the destination IP. True or false?
2. Workstation → `203.0.113.88:443`, `conn_state` `SF`. In one sentence, what occurred?
3. A SIEM query that matches every connection is a good “specific connection activity” query. True or false?

---

## 3. Summary

A `conn` event is who talked to whom, on which ports, and how it ended. State and history are on the wire. The process is not. A query names a specific pattern.

**Next:** **1.2.3** DNS engine.

---

## 4. Related modules

- 1.2.1 – Zeek concepts
- 1.2.3 – DNS engine
- 1.1.4 – Host-observed network

---

# Lesson 1.2.3 – DNS Engine

Source: `modules/01-soc/02-zeek/03-dns-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `dns` log: question, answer, record type, and who asked which DNS server.
2. Describe what a `dns` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

---

## 1. Key Concepts

SOC analysts read Zeek **`dns`** logs to see a name lookup on the **wire**. That is daily alert work: an alert names a domain or a lookup, and you have to say who asked, for which name, which type, and what came back. **1.2.2** was the connection. This lesson is the **DNS** extract. It does **not** name the initiating process. That was **1.1.4**. It is **not** TLS (**1.2.4**).

The DNS engine writes the **`dns`** log. Each log is one **event** for a query (and the response Zeek saw). In a SIEM, that event usually shows up as a **row** in a dns table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Query (question)** | `query` — the name that was asked |
| **Response (answer)** | `answers` — what came back (an address, another name, or empty) |
| **Record type** | `qtype_name` — **A**, **AAAA**, **MX**, **CNAME**, **NS**, **TXT**, and the rest when you see them |
| **Source / dest** | `id.orig_h` = who asked. `id.resp_h` = the DNS server that was asked |

`id.resp_h` is often a recursive resolver. It is **not** the address the name resolved to. That value, when present, is in `answers`.

| `qtype_name` | What was asked for |
|--------------|-------------------|
| **A** | IPv4 address |
| **AAAA** | IPv6 address |
| **MX** | Mail exchanger |
| **CNAME** | Another name (canonical name), not an address |
| **NS** | Name server |
| **TXT** | Text data |

A **CNAME** answer is another name, not an address. An empty `answers` list means this log does not show a returned record — say that. Do not invent NXDOMAIN hunting or DGA methodology here.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open TLS or HTTP fields yet.

**What good looks like:**

- Describe: one sentence — who asked, for which name, which type, what answered. Do not name a process. Do not call it C2 from a single A record.
- Given: `id.orig_h` a workstation, `query` a hostname, `qtype_name` `A`, `answers` `["203.0.113.88"]`. **What occurred:** that host asked for that name and got **A** `203.0.113.88`. The TCP connection to `:443` is a different log (**1.2.2**). Who launched the lookup is on the **host** (**1.1.4**).
- Query: names a **specific** pattern (`query`, `qtype_name`, or `answers`), not every `dns` event.

---

## 2. Knowledge Check

1. `id.resp_h` on a `dns` log is the IP the name resolved to. True or false?
2. Workstation queries a hostname, type `A`, answers `["203.0.113.88"]`. In one sentence, what occurred?
3. A SIEM query that matches every `dns` log is a good “specific DNS activity” query. True or false?

---

## 3. Summary

A `dns` log is the question, the type, the answer, and who asked which DNS server. The process is not on this log. A query names a specific pattern.

**Next:** **1.2.4** TLS engine.

---

## 4. Related modules

- 1.2.2 – Conn engine (previous)
- 1.2.4 – TLS engine
- 1.1.4 – Host-observed network

---

# Lesson 1.2.4 – TLS Engine

Source: `modules/01-soc/02-zeek/04-tls-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a TLS event: SNI, certificate subject and issuer, JA3 where logged, version, cipher, and who talked to whom.
2. Describe what a Zeek TLS log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

---

## 1. Key Concepts

SOC analysts read Zeek **TLS** events to see the **handshake** when the payload is encrypted. That is daily alert work: traffic on 443 still needs a description — who talked to whom, which hostname the client asked for, what name is on the certificate, and which version and cipher were negotiated. This lesson is the **TLS** engine. Zeek writes it to the **`ssl`** log (the name is historical). It is **not** decrypted HTTP. It does **not** name the initiating process. That is host-observed network (**1.1.4**).

Each handshake Zeek saw is one **event** in that log. In a SIEM, that event usually shows up as a **row**. Later lessons may still say “row.” Here it means the same thing as the TLS log.

| Idea | What to read |
|------|----------------|
| **SNI** | `server_name` — the hostname in the Client Hello. Empty means it was not sent or not logged. |
| **Subject / issuer** | `subject` / `issuer` — the name on the certificate, and who signed it. SNI is not the certificate subject. |
| **JA3 / JA3S** | Client / server TLS fingerprints **where the shop logs them**. Missing means not logged, not “no TLS.” |
| **Version / cipher** | `version`, `cipher` — what was negotiated |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` — originator to responder |

JA3 is how the client spoke TLS, not a malware name. Do not treat a JA3 value as a verdict. Do not invent a JA3 value. If the field is empty, say so.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open HTTP fields yet (**1.2.5**).

**What good looks like:**

- Describe: one sentence — who talked to whom, SNI if present, subject/issuer, version/cipher, JA3 only if logged. Do not name a process. Do not call it phishing from one SNI and subject mismatch.
- Given: `id.resp_h` `203.0.113.88`, `id.resp_p` `443`, `server_name` empty, `version` / `cipher` present. **What occurred:** that host completed a TLS handshake to `203.0.113.88:443`. SNI was not logged.
- Query: names a **specific** pattern (SNI, subject, version, or dest IP/port), not every `ssl` event.

---

## 2. Knowledge Check

1. `server_name` is the name on the server certificate. True or false?
2. Workstation → `203.0.113.88:443`, `server_name` empty, version and cipher present. In one sentence, what occurred?
3. A SIEM query that matches every `ssl` event is a good “specific TLS activity” query. True or false?

---

## 3. Summary

A TLS event is the handshake: SNI, certificate, version, cipher, and who talked to whom. JA3 only if logged. The process is not on this log. A query names a specific pattern.

**Next:** **1.2.5** HTTP engine.

---

## 4. Related modules

- 1.2.3 – DNS engine (previous)
- 1.2.5 – HTTP engine
- 1.2.2 – Conn engine
- 1.1.4 – Host-observed network

---

# Lesson 1.2.5 – HTTP Engine

Source: `modules/01-soc/02-zeek/05-http-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C ; 1.2.5.2 2b / 3c / 4c ; 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C ; 1.2.5.2 3c / 4c / 4c ; 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B ; 1.2.5.2 1a / 2b / 3c ; 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `http` log: method, host, URI, User-Agent, status, and who talked to whom.
2. Describe what an `http` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

---

## 1. Key Concepts

SOC analysts read Zeek **HTTP** logs to see a request and response on the **wire**. That is daily alert work: an alert names a web request, and you have to say which method, host, and URI were used, what status came back, and who talked to whom. **1.2.4** was the TLS handshake. This lesson is **HTTP**. It does **not** name the initiating process. That is host telemetry (**1.1.4**). It is **not** the file extract (**1.2.7**).

The **`http`** log is one **event** for a request/response pair Zeek parsed. In a SIEM, that event usually shows up as a row in an HTTP table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Method** | `method` — GET, POST, PUT, HEAD, and the rest when you see them |
| **Host** | `host` — the Host header. Empty means it was not logged. This is not the destination IP. |
| **URI / URL** | `uri` is the path and query. **Host + URI** is the URL you describe. There is often no single `url` field. |
| **User-Agent** | `user_agent` — what the client claimed. It can lie. Empty means it was not logged. |
| **Status** | `status_code` — 200 is not “benign.” 404 is not “safe.” |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` |

**How this shows up:** Zeek `http` (`method`, `host`, `uri`, `user_agent`, `status_code`, `id.orig_*`, `id.resp_*`).

You usually do **not** get the body. File extract is **1.2.7**. Encrypted HTTPS often has no `http` log — that is the `ssl` extract (**1.2.4**).

If a field is empty, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — method, host+URI, status, User-Agent if logged, orig → resp. Do not name a process. Do not invent the body.
- Given: `GET`, `uri` `/update.exe`, `id.resp_h` `203.0.113.88`, `id.resp_p` `8080`, `status_code` `200`, `user_agent` empty. **What occurred:** the originator requested **GET** `/update.exe` from `203.0.113.88` on port **8080** and received status **200**. User-Agent was not logged. Do not mix this with a TLS handshake (**1.2.4**).
- Query: names a **specific** pattern (method, host, URI, User-Agent, or dest), not every `http` log.

---

## 2. Knowledge Check

1. `host` is the destination IP. True or false?
2. `GET /update.exe` to `203.0.113.88:8080`, status `200`, User-Agent empty. In one sentence, what occurred?
3. A SIEM query that matches every `http` log is a good “specific HTTP activity” query. True or false?

---

## 3. Summary

An `http` log is method, host+URI, User-Agent, status, and who talked to whom. The process is not on this log. A query names a specific pattern.

**Next:** **1.2.6** SMTP engine.

---

## 4. Related modules

- 1.2.4 – TLS engine (previous)
- 1.2.6 – SMTP engine
- 1.2.7 – Files engine
- 1.1.4 – Host-observed network

---

# Lesson 1.2.6 – SMTP Engine

Source: `modules/01-soc/02-zeek/06-smtp-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C ; 1.2.6.2 2b / 3c / 4c ; 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C ; 1.2.6.2 3c / 4c / 4c ; 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B ; 1.2.6.2 1a / 1a / 2b ; 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `smtp` log: mail from, rcpt to, subject, message ID, and who talked to whom.
2. Describe what an `smtp` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`smtp`** log to see a mail transaction on the **wire**. That is daily alert work: an alert names a session, and you have to say who the session claimed mail was from and to, what subject was logged, and which hosts talked. It is **not** a mailbox. It is **not** the attachment bytes — those are **1.2.7**. It does **not** name the initiating process. That was **1.1.4**.

**SMTP activity** is network-sensor telemetry about a mail transaction Zeek parsed: envelope sender, envelope recipients, a few headers, and who talked to whom. In a SIEM, that event usually shows up as a row in an `smtp` table.

| Idea | What to read |
|------|----------------|
| **Mail from** | `mailfrom` — envelope MAIL FROM. Who the *session* claimed as sender. Not the From header. |
| **Rcpt to** | `rcptto` — envelope RCPT TO (can be more than one address) |
| **Subject** | `subject` — the Subject header. Empty = not logged. Easy to spoof. |
| **Message ID** | `msg_id` — Message-ID when logged. Not a file hash. |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` (often 25 / 587) |

Zeek watches the wire and writes this log. Encrypted submission may have no SMTP fields — that handshake was **1.2.4**. Empty `subject` or `msg_id` means not logged, not “no mail.” Do not invent a mail-gateway name.

**What good looks like:**

- Describe: one sentence — envelope from, envelope to, subject if logged, orig → resp. Do not name a process. Do not declare phishing.
- Given: `mailfrom` an outside address, `rcptto` a user, `subject` present, `msg_id` present. **What occurred:** that client sent envelope mail from A to B with that subject.
- Query: names a **specific** pattern (`mailfrom`, `rcptto`, subject, or dest), not “all `smtp` events.”

---

## 2. Knowledge Check

1. `mailfrom` is the attachment hash. True or false?
2. Envelope from an outside address, `rcptto` a user, subject present. In one sentence, what occurred?
3. A SIEM query that matches every `smtp` event is a good “specific SMTP activity” query. True or false?

---

## 3. Summary

An `smtp` log is envelope from/to, subject, message ID, and who talked to whom. The process and the attachment hash are not on this event. A query names a specific pattern.

**Next:** **1.2.7** Files engine.

---

## 4. Related modules

- 1.2.5 – HTTP engine (previous)
- 1.2.7 – Files engine
- 1.2.4 – TLS engine
- 1.1.4 – Host-observed network

---

# Lesson 1.2.7 – Files Engine

Source: `modules/01-soc/02-zeek/07-files-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C ; 1.2.7.2 2b / 3c / 4c ; 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C ; 1.2.7.2 3c / 4c / 4c ; 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B ; 1.2.7.2 1a / 1a / 2b ; 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek **files** event: name, MIME type, hash, who sent and received it, and the connection UID that joins other Zeek logs.
2. Describe what a `files` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

---

## 1. Key Concepts

SOC analysts read the Zeek **files** log to see a file on the **wire**. An alert may name a download, an attachment, or a hash. The job in this lesson is to say what moved: the name if the protocol gave one, the MIME type, the hash if Zeek calculated it, who sent it, and who received it. **1.2.1** said engines extract protocol. This lesson is the **files** engine. It is **not** host file activity (**1.1.3**). It is **not** YARA (**1.3**).

The **files** log is one **event** for a file Zeek analyzed on the wire. In a SIEM, that event usually shows up as a **row** in a files table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **File name** | `filename` — when the protocol gave one. It can lie. Empty means not logged. |
| **MIME type** | `mime_type` — what Zeek thinks the bytes are (for a Windows executable, often `application/x-dosexec`). It can disagree with the name. |
| **Hash** | `md5` / `sha1` / `sha256` when calculated. Empty is not “clean.” Do not invent a hash. |
| **Source / dest** | `tx_hosts` sent the bytes. `rx_hosts` received them. These are not `id.orig_h` / `id.resp_h`. |
| **Connection UID** | `conn_uids` — those values *are* the `uid` on `conn` / `http` / `smtp`. Copy one and search. |

This is the **extract**. Zeek does not have to write the bytes to disk. The host may or may not create a file. A Temp path on the host is a different sensor (**1.1.3**).

**What good looks like:**

- Describe: one sentence — name if logged, MIME, hash if logged, who sent to whom. Then say which `uid` you would open on `conn` or `http`. Do not describe a Sysmon 11.
- Given: `filename` `update.exe`, `mime_type` `application/x-dosexec`, `sha256` present, `tx_hosts` `203.0.113.88`, `rx_hosts` a workstation, `conn_uids` present. **What occurred:** that IP sent `update.exe` (executable MIME, hash logged) to that host on the wire. Copy `conn_uids` and search the other Zeek logs. The Temp file-create is **1.1.3**.
- Query: names a **specific** pattern (name, MIME, hash, or tx/rx), not every `files` event.

---

## 2. Knowledge Check

1. A Zeek `files` event is the same thing as a Sysmon 11 file create. True or false?
2. `update.exe`, MIME `application/x-dosexec`, hash logged, from `203.0.113.88` to a workstation. In one sentence, what occurred?
3. A SIEM query that matches every `files` event is a good “specific file transfer” query. True or false?

---

## 3. Summary

A `files` event is a transfer on the wire: name, MIME, hash, who sent and received. `conn_uids` joins `conn` / `http` / `smtp`. The host file event is a different sensor.

**Next:** **1.2.8** Weird engine.

---

## 4. Related modules

- 1.2.6 – SMTP engine (previous)
- 1.2.5 – HTTP engine
- 1.2.8 – Weird engine
- 1.1.3 – File system activity (host)

---

# Lesson 1.2.8 – Weird Engine

Source: `modules/01-soc/02-zeek/08-weird-engine/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C ; 1.2.8.2 2b / 3c / 4c ; 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C ; 1.2.8.2 3c / 4c / 4c ; 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A ; 1.2.8.2 1a / 1a / 1a ; 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek **weird** log: the type, who talked to whom, and the UID that joins other Zeek logs.
2. Describe what a **weird** log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

---

## 1. Key Concepts

SOC analysts read the Zeek **weird** log when the sensor saw protocol behavior that is off-spec or uncommon. That is daily alert work: a log names a type, two endpoints, and often a connection ID, and you have to say what Zeek flagged — not whether it is an incident. A **weird** event is a **lead**, not a verdict. It does **not** name the initiating process. That was **1.1.4**.

Zeek watches the **wire**. Each **weird** log is one **event**. In a SIEM, that event usually shows up as a **row** in a table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Type / notice** | `name` — the weird type (the string you query). `notice` is a boolean: whether *this* type was also raised as a notice. This is **not** a `notice.log` lesson. |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` |
| **Connection UID** | `uid` — the same join as `conn`, `http`, and `files`. Empty → write “no uid” and use IP, port, and time if they are logged. |

Do not memorize the Zeek catalog. Describe the `name` you have. Do not invent a story from the word “weird.” Many types fire on noisy, broken, or mid-stream traffic.

This lesson only reads the **weird** log. It is not a PCAP analysis lesson. Detection rule syntax is **1.3**.

**What good looks like:**

- Describe: one sentence — Zeek flagged this `name` between these IPs/ports. Then say which `uid` you would open on `conn`. Do not call it malware.
- Given: `name` `data_before_established`, `id.resp_h` `203.0.113.88`, `id.resp_p` `8080`, `uid` present. **What occurred:** Zeek saw data before the TCP handshake finished to `203.0.113.88:8080`. Open `conn` on that `uid`. Do not name a process.
- Query: names a **specific** `name` (or dest), not every **weird** event.

---

## 2. Knowledge Check

1. A single **weird** event is an incident. True or false?
2. `name` `data_before_established`, dest `203.0.113.88:8080`, `uid` present. In one sentence, what occurred?
3. A SIEM query that matches every **weird** event is a good “specific weird activity” query. True or false?

---

## 3. Summary

A **weird** event is a type, two endpoints, and a UID. It is a lead. The process is not on this log. A query names a specific type.

**Next:** **1.3.1** SIGMA rules.

---

## 4. Related modules

- 1.2.7 – Files engine (previous)
- 1.2.2 – Conn engine
- 1.1.4 – Host-observed network
- 1.3.1 – SIGMA rules

---

# Lesson 1.3.1 – SIGMA Rules

Source: `modules/01-soc/03-detection/01-sigma-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B ; 1.3.1.2 1a / 2b / 3c ; 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a SIGMA rule: purpose, structure, field tests (selectors), and how it becomes a SIEM query.
2. Describe what an existing rule detects, and say what a **basic** create or modify looks like.

**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

---

## 1. Key Concepts

An alert comes from a **detection**. Someone wrote what to look for. SOC analysts **read** that write-up and **propose** a basic create or modify so detection engineering can review it. The shop may not all use the same SIEM, so **SIGMA** lets you write the idea once in YAML. A person or a converter turns it into that SIEM's query. You do **not** deploy the rule. How detections run as a service is **4.x**.

This lesson is SIGMA. It is not Suricata, YARA, or a saved SIEM rule (**1.3.2**–**1.3.4**).

**SIGMA** is a generic detection format. You write what to look for once. A converter or a person turns it into a SIEM query.

| Idea | What to read |
|------|----------------|
| **Purpose / structure** | `title`, `logsource` (which telemetry), `detection` (named selections plus a `condition`). Without those, it is not a detection. |
| **Fields / selectors** | Field tests: `endswith`, `contains`, a list, `re`. Field names must match the logsource. `Image` / `CommandLine` on `process_creation` are process-create fields (**1.1.2**). Tests in one selection are typically **and**. A list under one field is typically **or**. |
| **To SIEM** | `logsource` → table or event type. Selections → `where`. `condition` → and / or / not. Write that in words or a SIEM-shaped sentence. Running a converter is not this lesson. |

**What good looks like:**

- Analyze: name logsource, selectors, condition, and what would fire. Do not invent a Zeek field on a Windows process rule.
- Given:

```yaml
title: Encoded PowerShell from Script Host
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains: '-enc'
    ParentImage|endswith: '\wscript.exe'
  condition: selection
```

**What it detects:** process create — PowerShell with `-enc` and parent `wscript`. Same story as **1.1.2**. SIEM shape: `DeviceProcessEvents` / Sysmon 1, those three predicates.

- Modify / create: a **basic** rule with title, logsource, one selection, and a condition. Tightening “any `powershell.exe`” by adding parent or `-enc` is a modify. SOC **proposes**. Detection engineering reviews.

---

## 2. Knowledge Check

1. SIGMA is a SIEM product. True or false?
2. A `process_creation` rule matches `powershell.exe`, CommandLine `-enc`, and parent `wscript`. In one sentence, what does it detect?
3. Why is a rule that matches every `powershell.exe` a poor proposal?

---

## 3. Summary

SIGMA is portable YAML: logsource, selectors, condition. It becomes a SIEM query. You read it and propose a basic one. You do not deploy it.

**Next:** **1.3.2** Suricata rules.

---

## 4. Related modules

- 1.2.8 – Weird engine (previous)
- 1.1.2 – Process activity
- 1.3.2 – Suricata rules
- 1.3.4 – SIEM rules
- 4.x – How detections run as a service

---

# Lesson 1.3.2 – Suricata Rules

Source: `modules/01-soc/03-detection/02-suricata-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B ; 1.3.2.2 1a / 2b / 3c ; 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name action, header, and options on a Suricata rule, and say how a hit relates to a Zeek log of the same session.
2. Read an existing rule and say what it detects; propose a **basic** create or modify.

**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

---

## 1. Key Concepts

SOC analysts read a **network signature** to see what on the wire would fire. That is daily alert work: an alert names a Suricata rule, and you have to say what it matches — protocol, direction, and the string or buffer it looks for — and whether that match is specific. **1.3.1** was portable YAML for host logs (SIGMA). This lesson is **Suricata**: packets and streams. You do **not** deploy it. How detections run as a service is **4.x**. It is **not** YARA (**1.3.3**).

**Suricata** inspects packets and streams and can **alert** when a signature matches. This lesson uses `alert` only — not drop or reject.

```
alert proto src_ip src_port -> dst_ip dst_port ( options )
```

| Idea | What to read |
|------|----------------|
| **Action, header, options** | Action = `alert`. Header = protocol, addresses, ports, and `->`. Options = `msg`, `sid`, `rev`, and the match keywords |
| **Common options** | `content:"..."`. HTTP buffers: `http.uri`, `http.method`, `http.user_agent`. TLS: `tls.sni` (the name the client asked for). `flow:established,to_server` means an established connection, client to server |
| **ASCII / hex / regex** | ASCII = `content:"/update.exe"`. Hex = `content:"\|4d 5a\|"` (the two bytes `MZ` that start a Windows executable). Regex = `pcre:"/update\\.(exe\|dll)/i"`. Regex is easy to over-match. Do not paste exploit payloads |
| **Vs Zeek** | Zeek writes parsed fields for the session (method, URI, who talked). Suricata writes that this signature matched. The same session can produce both. Join them with time plus the **5-tuple** (source IP, source port, destination IP, destination port, protocol). Do not put Zeek field names (`uri`, `id.orig_h`, `uid`) in the Suricata rule |

`$HOME_NET` means our network. `$EXTERNAL_NET` means not our network. Both are **site variables**. Do not invent the address range.

**What good looks like:**

- Analyze: name action, header, options, and what would fire. A raw `content:"GET"` on `tcp any any` is too broad — those three bytes match anywhere in any TCP session.
- Given:

```
alert http $HOME_NET any -> $EXTERNAL_NET any (
  msg:"GET /update.exe";
  flow:established,to_server;
  http.method; content:"GET";
  http.uri; content:"/update.exe";
  sid:1000001; rev:1;)
```

**What it detects:** outbound HTTP GET whose URI contains `/update.exe`. A matching session should also have a Zeek `http` log of that GET.

- Modify / create: a **basic** `alert` with a header, `msg`, `sid`, `rev`, and one specific `content` in the right buffer. Tightening “any GET” by adding `http.uri` is a modify. SOC **proposes**. Detection Engineering reviews.

---

## 2. Knowledge Check

1. Suricata and Zeek do the same job on a session. True or false?
2. The given rule above — what does it detect, in one sentence?
3. Why is `content:"GET"` on `tcp any any` a poor proposal?

---

## 3. Summary

A Suricata rule is action, header, and options. Put the match in the right buffer. ASCII, hex, and regex are techniques. Zeek tells you the session; Suricata tells you the signature matched. You propose. You do not deploy.

**Next:** **1.3.3** YARA rules.

---

## 4. Related modules

- 1.3.1 – SIGMA rules (previous)
- 1.2.5 – HTTP engine
- 1.3.3 – YARA rules
- 4.x – How detections run as a service

---

# Lesson 1.3.3 – YARA Rules

Source: `modules/01-soc/03-detection/03-yara-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B ; 1.3.3.2 1a / 2b / 3c ; 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what a YARA rule is for, name its blocks, and when it runs on a file vs memory.
2. Read an existing rule and say what it detects; propose a **basic** create or modify.

**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

---

## 1. Key Concepts

SOC analysts match **byte patterns** on a file they already have, or on memory the shop already scans. A log can name a file, a hash, or a URI. It does not show the bytes inside. That is the job in this lesson: read a **YARA** rule so you can say what would hit those bytes, and propose a basic create or modify. **1.3.2** was Suricata on the wire. This lesson is the file (or memory). You do **not** deploy the rule. You do **not** dump memory. How detections run as a service is **4.x**.

**YARA** matches **byte patterns** in a file or in process memory. It is not SIGMA and not Suricata. It is not a SIEM query language.

```
rule RuleName
{
    meta:
        description = "..."
    strings:
        $a = "..."
    condition:
        $a
}
```

| Idea | What to read |
|------|----------------|
| **Purpose / structure** | `rule` name, `meta` (notes, not the match), `strings`, `condition`. A strings block with no real condition is not a useful proposal. |
| **Strings and condition** | Named patterns plus boolean (`and`, `or`, `filesize`, `uint16(0) == 0x5A4D`, `#s >= 2`). `$mz at 0` is the same *idea* as that `uint16` check: MZ at the start of the file. |
| **ASCII / hex / regex** | ASCII = `"update.exe" ascii nocase`. Hex = `{ 4D 5A }` (`MZ`) — not Suricata `content:"\|4d 5a\|"`. Regex = `/update\.(exe\|dll)/ nocase`. Regex is easy to over-match. |
| **Files vs memory** | **File** — disk or a saved extract. `at 0` and `filesize` can apply. **Memory** — a process the shop already scans. Drop `filesize` (it does not apply there, so the rule will not match). Drop `at 0` for a PE header; the image may not sit at the start of the region. If your shop does not scan memory, say so and stay on files. |

**What good looks like:**

- Analyze: name the strings, the condition, file vs memory, and what would fire. `{ 4D 5A } at 0` alone matches every PE, including Notepad.
- Given:

```
rule Train_UpdateExe
{
    meta:
        description = "PE that contains update.exe"
    strings:
        $mz = { 4D 5A }
        $name = "update.exe" ascii nocase
    condition:
        $mz at 0 and $name and filesize < 5MB
}
```

**What it detects:** a **file** that starts with MZ and contains `update.exe`, under 5 MB. That can fit a PE extract of `update.exe` (**1.2.7**) **if you scan those bytes**. It does not match a `files` log line. It is not a conviction.

- Modify / create: a **basic** file rule with one distinctive string **and** a header or size check. Tightening “MZ only” by adding `update.exe` is a modify. SOC **proposes**. DE reviews.

---

## 2. Knowledge Check

1. YARA is a SIEM query language. True or false?
2. The given rule above — what does it detect, in one sentence?
3. Why is `{ 4D 5A } at 0` alone a poor proposal?

---

## 3. Summary

YARA is meta + strings + condition. ASCII, hex, and regex. File rules may use `at 0` and `filesize`. Memory often must not. You propose. You do not deploy.

**Next:** **1.3.4** SIEM rules.

---

## 4. Related modules

- 1.3.2 – Suricata rules (previous)
- 1.2.7 – Files engine
- 1.3.4 – SIEM rules
- 4.x – How detections run as a service

---

# Lesson 1.3.4 – SIEM Rules

Source: `modules/01-soc/03-detection/04-siem-rules/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the pieces of a SIEM detection, and how log fields (or a SIGMA rule) become one.
2. Read an existing SIEM rule and say what it detects; propose a **basic** create from fields or from SIGMA.

**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

---

## 1. Key Concepts

SOC analysts **read** a saved detection and **propose** a basic one. That is daily work: an alert names a rule, and you have to say what that rule looks at — which table, which fields, which match — before you treat the alert as a fact. This lesson is that saved rule. It is **not** opening the alert (**1.4**). It is **not** how detections run as a service (**4.x**). You **propose**. You do **not** deploy.

A **SIEM rule** is named logic that runs on ingested logs and can fire an alert. Shops also call this an **analytics rule** or a **correlation search**. Here those names mean the saved detection, not a requirement to join events.

| Idea | What to read |
|------|----------------|
| **Structure** | **Name**, **table** (which log store), **logic** (the filter), **window** (how far back / how often), **output** fields. A table with no filter is not a detection. A join or count across events in a window is extra. A basic rule can be a filter on one table. |
| **Fields → detection** | Name the table. Pick fields that exist on that table (`FileName`, `ProcessCommandLine` on process events). Add a parent, token, or destination so it is not “all PowerShell.” |
| **Wildcards / regex** | **Wildcard** or substring when a path or fixed token is enough (`*\\Temp\\*`, `-enc`). **Regex** when the token itself varies (`-e` / `-enc` / `-EncodedCommand`). Do not regex an empty field into existence. |

**From SIGMA (second create path):** SIGMA is a portable detection: you write what to look for once. Turn it into a SIEM rule by mapping **logsource** (which telemetry) → table, **selectors** (field tests) → logic, **condition** (and / or / not) → how those tests combine. Then name it, give it a window, and list output fields. You are not required to run a converter.

**What good looks like:**

- Analyze: name table, logic, window, and what would fire.
- Given:

```
Name: Encoded PowerShell from script host
Source: DeviceProcessEvents
Window: 5 minutes
Logic:
  FileName =~ "powershell.exe"
  and ProcessCommandLine has "-enc"
  and InitiatingProcessFileName == "wscript.exe"
Output: Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessCommandLine
```

**What it detects:** a process create of PowerShell with `-enc` in the command line, parent `wscript`.

If you started from SIGMA, the same three tests were `Image` / `CommandLine` / `ParentImage` on `process_creation`. The SIEM wrap is the name, table, window, and outputs.

- Create: a **basic** proposed rule from those fields **or** from that SIGMA mapping. An unfiltered `DeviceProcessEvents` is not a create. SOC **proposes**. Detection engineering reviews.

---

## 2. Knowledge Check

1. A SIEM table with no filter is a detection. True or false?
2. The given rule above — what does it detect, in one sentence?
3. When do you use a wildcard instead of a regex?

---

## 3. Summary

A SIEM rule is named logic on a table, in a window, with outputs. Build it from fields you know, or translate SIGMA. You propose. You do not deploy.

**Next:** **1.4.1** Alert context and investigation.

---

## 4. Related modules

- 1.3.1 – SIGMA rules
- 1.3.3 – YARA rules
- 1.1.2 – Process activity
- 1.4.1 – Alert context and investigation
- 4.x – How detections run as a service

---

# Lesson 1.4.1 – Alert Context and Investigation

Source: `modules/01-soc/04-alerts/01-context-investigation/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2 1a / 1a / 2b ; 1.4.1.3 1a / 1a / 2b ; 1.4.1.4 1a / 1a / 2b ; 1.4.1.5 1a / 1a / 1a ; 1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Review an alert: name the context that is present and missing (including a VirusTotal lookup of a hash, IP, or domain you have), say what the configuration would fire, and name each hop upstream.
2. Say what related endpoint logs and PCAP **add** — or fail to add — versus the alert fields.

**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 – Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have)
- T: 1.4.1.3 – Review the alert configuration and explain what would fire
- T: 1.4.1.4 – Trace an alert to its upstream detection logic and name each hop
- T: 1.4.1.5 – Collect related endpoint logs and state what they add (or fail to add)
- T: 1.4.1.6 – Collect related PCAP and state what it adds versus the alert fields

---

## 1. Key Concepts

SOC analysts work the **alert that fired** — the object in the queue — before they label it true or false. A detection created that alert. Before you classify it, you have to say what it already shows, what it does not, what the rule would fire on, how it reached the queue, and what related host logs or a packet capture add. That is the job in this lesson: gather that context so you do not treat a gap as benign or invent a hop that is not there.

**1.3** taught how to read and propose a detection. This lesson you do **not** write a new rule. You do **not** classify TP/FP (**1.4.2**).

The first alert in this course is the **process create**: `wscript` → encoded PowerShell as `jlee`. That is what the **1.3.4** SIEM rule keys on.

| Idea | What to do |
|------|------------|
| **Context** | Two lists: **present** and **missing**. Typical present fields are host, user, time, rule name, and the field the rule keys on. If you have a **hash**, **IP**, or **domain**, look it up on **VirusTotal** (**0.7**). Write what VT adds or fails to add (reputation, or “not in VT”). That is gathering context, not opening Relations or a pivot graph (**2.9**). Missing is a **gap**, not “benign.” Do not invent a command line or a VT hit. |
| **Configuration** | Read the detection behind the alert. One sentence: **what would fire**. Use the same field language as **1.3**. |
| **Upstream hops** | Name each hop from detection logic to the alert. Classroom pattern: Suricata rule → SIEM correlation search → SIEM alert. Some alerts are SIEM-only. Do not invent a Suricata hop. |
| **Endpoint logs** | Pull related **1.1** host events for that host and time window. State what they **add** or **fail to add**. Opening the table is not the task. A file event for Temp `invoice.vbs` can add the dropper path. The Run key is **not** required on this first pass (hunt is **3.x**). |
| **PCAP** | For a **network** alert: state what the capture adds versus the alert fields (URI, SNI, payload). Why you pull PCAP is **1.2.1**. Where sensors sit is **0.8**. If the alert is process-only and no capture exists, write **PCAP not applicable**. Do not invent a download path. |

**What good looks like:**

- **Context:** Present = host, user, rule, `powershell -enc`, parent `wscript`. Missing until you pull more = dest IP, URI, file hash. After a file event adds Temp `invoice.vbs` (or you have `203.0.113.88`), look that hash or IP up on **VirusTotal**. Write the one-line result. Do not open Relations.
- **Config:** “PowerShell with `-enc` and parent `wscript` fires.”
- **Hops:** SIEM rule → SIEM alert (no Suricata unless the given includes a Suricata rule).
- **Endpoint logs:** A Sysmon 11 / `DeviceFileEvents` file event **adds** Temp `invoice.vbs`. If the tenant has no process parent, the logs **fail to add** it — say so.
- **PCAP:** On a `:8080` GET, PCAP can **add** the URI `/update.exe` if the alert only had IP:port. On this process alert, PCAP is **not applicable** until you have a flow.

---

## 2. Knowledge Check

1. The alert context is missing a parent process. That means the activity was benign. True or false?
2. Name the hops for a SIEM-only process alert.
3. You have the hash of Temp `invoice.vbs` and IP `203.0.113.88`. What do you look up on VirusTotal, and what is **not** this lesson?

---

## 3. Summary

Present versus missing. A hash, IP, or domain you have goes to **VirusTotal**. Say what the configuration would fire. Name each hop. Endpoint logs and PCAP must **add** something — or you say they failed to. You do not classify, and you do not write the rule.

**Next:** **1.4.2** Alert classification.

---

## 4. Related modules

- 1.3.4 – SIEM rules (previous)
- 1.4.2 – Alert classification
- 1.1.2 – Process activity
- 1.1.3 – File system activity
- 1.2.1 – Zeek concepts (why pull PCAP)
- 0.7 – External tools (VirusTotal)
- 0.8 – Environment / signal flow

---

# Lesson 1.4.2 – Alert Classification

Source: `modules/01-soc/04-alerts/02-classification/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define **True Positive (TP)**, **False Positive (FP)**, **True Negative (TN)**, and **False Negative (FN)**.
2. Classify a given case and **cite the evidence**, including at least one miss as FN.

**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

---

## 1. Key Concepts

After you have looked at a case, you still have to **classify** it. A classification says whether the detection was right — a real hit, a noisy fire, ordinary activity that correctly stayed quiet, or a miss. You also **cite the evidence**: a short pointer to the field or log that proves the label. That is the job in this lesson. Without a label, the next person cannot tell a real hit from a miss. Without a cite, “malicious” is a slogan.

**1.4.1** gathered context on a fired alert. This lesson is the four labels. It is **not** why a false positive fired (**1.4.3**). It is **not** scan / root / user (**1.4.4**).

Fired alerts sit in an **alert queue** — the list waiting for an analyst. True negatives and false negatives usually are **not** in that list, because nothing fired.

| Label | Detection said | Reality |
|-------|----------------|---------|
| **True Positive (TP)** | Bad | Bad — a fired alert, and the activity is what the rule is for |
| **False Positive (FP)** | Bad | Benign — a fired alert, authorized or expected activity |
| **True Negative (TN)** | Not bad | Benign — **no alert**, ordinary activity |
| **False Negative (FN)** | Not bad | Bad — **no alert**, activity that should have been detected |

A **false negative is not a fired alert you dislike.** It is a **miss**. You find it in related logs, in a hunt, or after an incident — not as a fired alert in the queue.

**Evidence** is a short cite: parent plus `-enc`, destination plus URI, “no alert on that GET.” A slogan (“malicious”) is not evidence.

**What good looks like:** someone gives you a case. You name TP, FP, TN, or FN. You point at the field or log that proves it.

- **TP:** Alert `Encoded PowerShell from script host`. Cite: `wscript` plus `-enc` is the activity the rule is for, and it happened (**1.4.1**).
- **FP:** Alert on any PowerShell; logs show interactive `Get-Help`. Cite: PowerShell ran; it is ordinary help, not encoded script-host. *Why* the rule is broad is **1.4.3**.
- **TN:** No alert on ordinary browser activity. Cite: expected browse, no matching bad pattern. Do not invent an alert so you can classify it.
- **FN:** HTTP shows `GET /update.exe` to `203.0.113.88:8080`, **no** alert in the queue. Cite: the download occurred; nothing fired. That is a miss.

Do not pick a category yet (**1.4.4**). Do not explain why the false-positive rule is noisy (**1.4.3**).

---

## 2. Knowledge Check

1. FN is a bad alert sitting in the queue. True or false?
2. Alert `Encoded PowerShell from script host`, `wscript` + `-enc` confirmed. Classify and cite.
3. `GET /update.exe` to `203.0.113.88:8080`, no alert. Classify and cite.

---

## 3. Summary

Four labels. A true negative and a false negative usually have **no** alert in the queue. Classify the case and cite the evidence. Why a false positive fired is next.

**Next:** **1.4.3** Common false positive causes.

---

## 4. Related modules

- 1.4.1 – Alert context and investigation (previous)
- 1.4.3 – Common false positive causes
- 1.1.2 – Process activity
- 1.2.5 – HTTP engine

---

# Lesson 1.4.3 – Common False Positive Causes

Source: `modules/01-soc/04-alerts/03-false-positive-causes/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C ; 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C ; 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B ; 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two cause classes: analyst or tool activity, and untuned or overly broad detection logic.
2. Given a false positive, pick the class and say **what you would change**.

**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

---

## 1. Key Concepts

SOC analysts still have work after they call an alert a **false positive**. That fire already used queue time, and the same benign activity will fire again unless someone says why it matched and what would stop it. That is the job in this lesson: pick a **cause class** and name **one change**. You do not decide true positive versus false positive again. You do not deploy the change.

A false positive is a fired alert on authorized or expected activity. Classification (**1.4.2**) already put that label on the case. This lesson is the **cause** of that fire, not the label. Categories such as scan, root, or user are **1.4.4**.

| Cause class | What it looks like | Change you can name |
|-------------|--------------------|---------------------|
| **Analyst or tool activity** | A security analyst downloaded or tested a rule that is already live; packet replay into production; a scanner the shop owns | Exclude the lab, replay, or scanner identity; test in a lab window. Do not delete a good signature |
| **Untuned or overly broad detection logic** | Any PowerShell; `content:"GET"` on any TCP; MZ-only YARA wired to an alert | Add a second selector (parent and `-enc`); bind an HTTP buffer; raise a threshold |

Those two classes are the ones this lesson teaches. If neither fits, say **other — not analyst/tool or overly broad** and still name a change. Do not invent a third official class.

A change is one concrete sentence: “Require parent `wscript` and `-enc`.” “Tune it” is not a change. You name the change. Detection engineering deploys it (**1.3** / **4.x**).

**What good looks like:**

- **Overly broad:** False positive on any-PowerShell / `Get-Help` (**1.4.2**). Class: untuned or overly broad detection logic. Change: require `-enc` and a script-host parent. Hand it to detection engineering.
- **Analyst or tool:** False positive because an analyst replayed yesterday’s `GET /update.exe` packet capture into production. Class: analyst or tool activity. Change: exclude the replay window or interface. Do not delete the `/update.exe` signature.

---

## 2. Knowledge Check

1. This lesson is for deciding true positive versus false positive. True or false?
2. What are the two cause classes?
3. False positive: any-PowerShell on `Get-Help`. Name the class and one change sentence.

---

## 3. Summary

After a false positive: **class + change**. Analyst or tool activity versus untuned or overly broad logic. Name the change. You do not deploy it.

**Next:** **1.4.4** Common alert categorizations.

---

## 4. Related modules

- 1.4.2 – Alert classification (previous)
- 1.4.4 – Common alert categorizations
- 1.3.1 – SIGMA rules
- 4.x – How detections run as a service

---

# Lesson 1.4.4 – Common Alert Categorizations

Source: `modules/01-soc/04-alerts/04-categorizations/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C ; 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C ; 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A ; 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the syllabus categories: scanning / reconnaissance, root-level access, user-level access, unsuccessful activity, and **other** as your shop uses it.
2. Assign a category and **justify why it is not the adjacent category**.

**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category to an alert and justify why it is not the adjacent category

---

## 1. Key Concepts

SOC analysts put a **category** on an alert so the next desk can see what kind of activity it was. A true-positive or false-positive label only says whether the detection was right. A category says whether this was a scan, a failed attempt, or access as a user versus as an administrator. You pick one name and say why the **adjacent category** — the neighbor people mix it up with — is wrong. You do **not** re-argue true positive versus false positive (**1.4.2**). You do **not** name a false-positive cause (**1.4.3**). You do **not** write an ATT&CK technique ID as the category (**0.6**).

| Category | Use when | Adjacent — not this |
|----------|----------|---------------------|
| **Scanning / reconnaissance** | Wide, unauthenticated probing (many ports or hosts; no login or exploit attempt) | **Unsuccessful** — a failed login is an access *attempt*, not a sweep |
| **Root-level access** | SYSTEM, admin, or service-level control on the host | **User-level** — the same command as a standard user is not root |
| **User-level access** | Activity as a normal user account (Windows Medium integrity — `jlee`) | **Root-level** — encoded or “looks like malware” does not upgrade the account |
| **Unsuccessful activity** | An access or exploit *attempt* that failed (denied logon; HTTP 401 burst on one app) | **Scanning** — failed authorization is not a port sweep |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent ATT&CK tactics as categories |

The adjacent pairs are **scan ↔ unsuccessful** and **user ↔ root**. The task is two sentences: **category**, then **not the neighbor because …**.

**What good looks like:**

- **User-level, not root:** Alert `Encoded PowerShell from script host`, `wscript` + `-enc` as Medium `jlee` (**1.4.1**). Category **user-level**. Not root: the account is a standard user. Encoded does not change the category. (The same command as **SYSTEM** after a service start would be **root**, not user.)
- **Scanning, not unsuccessful:** Given: many unanswered SYN to 150 ports in two minutes, no login. Category **scanning / reconnaissance**. Not unsuccessful: nothing was presented as credentials or an exploit — it is a sweep.

Do not invent a DYA category list here. If you need **other**, use a name your real shop already has.

---

## 2. Knowledge Check

1. A category is the same thing as a true-positive or false-positive label. True or false?
2. Name the four syllabus categories plus **other**.
3. Alert: `wscript` + `-enc` as Medium `jlee`. Category, and why not the adjacent one?

---

## 3. Summary

A category names the kind of activity and rejects the neighbor. A scan is not failed authorization. A user account is not root. Other is a name your shop already uses.

**Next:** **1.4.5** Service Level Agreements / Response Time Goals.

---

## 4. Related modules

- 1.4.3 – Common false positive causes (previous)
- 1.4.5 – SLA / response time goals
- 1.4.2 – Alert classification
- 0.6 – Frameworks (ATT&CK is not a category)

---

# Lesson 1.4.5 – SLA / Response Time Goals

Source: `modules/01-soc/04-alerts/05-sla-response-times/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C ; 1.4.5.2 2b / 3c / 4c ; 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B ; 1.4.5.2 1a / 2b / 3c ; 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A ; 1.4.5.2 1a / 1a / 1a ; 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two clocks: time to **begin** investigation, and time to **close or escalate**.
2. Given timestamps, say **which clock is at risk**.
3. Close or escalate and **record it against the correct clock**.

**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Given timestamps, identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

---

## 1. Key Concepts

SOC analysts keep an alert from sitting untouched, and from sitting open with no close or escalate. That is the job in this lesson: name **which** response-time goal is at risk, then record closed or escalated against it. “Work faster” is not the task.

A **service-level agreement (SLA)** here is a **response-time goal**: the maximum time allowed for a step. This lesson uses two **clocks** — the short word for those goals.

| Clock | What it measures | Classroom goal |
|-------|------------------|----------------|
| **Start** | Alert **created** → first touch (`started`) | **15 minutes** |
| **Close / escalate** | First touch → `closed` or `escalated` | **45 minutes** |

The 15-minute and 45-minute figures are **this lesson only**. They are not a live shop policy. If your real shop uses different minutes, use those. The obligation is **two clocks**, not 15 and 45.

If nobody has touched the alert, only the **start** clock exists. Close/escalate has no origin until a first touch. After a first touch, start is already met (or already breached); the remaining clock is **close/escalate**.

This is **not** re-investigating the alert (**1.4.1**). It is **not** true-positive / false-positive or a category (**1.4.2**, **1.4.4**). It is **not** a report, and it is **not** the report clocks in **1.5**.

**Record** is one classroom line: **closed** or **escalated**, **which clock**, and the **time**. If you have not touched the alert yet, the first line is **started** against the **start** clock. Do not close an untouched alert to “meet SLA.” This is a classroom line, not a ticketing-product class.

**What good looks like:**

- **Start at risk:** Created `14:00`. No `started`. Now `14:18`. Clock: **start** (18 minutes, past 15). Close/escalate has no origin. Record: `started | start (breached) | 14:18`. Then investigate. Do not write `closed` yet.
- **Close/escalate at risk:** An alert first touched at `13:28` is still open at `14:20`. Clock: **close/escalate** (52 minutes since start, past 45). Start already met. Record: `escalated | close-escalate (breached) | 14:20` — or `closed` if the investigation is actually done.

---

## 2. Knowledge Check

1. If nobody has touched the alert, which clock can be at risk?
2. What are the two clocks, and when does each start?
3. An alert was first touched at `13:28` and is still open at `14:20`. Which clock is at risk, and what do you record?

---

## 3. Summary

Two clocks: **start** from created; **close/escalate** from first touch. Name the clock. Record closed or escalated against it.

**Next:** **1.5.1** Report types. This closes unit **1.4**.

---

## 4. Related modules

- 1.4.4 – Common alert categorizations (previous)
- 1.5.1 – Report types
- 1.4.1 – Alert context and investigation
- 1.5.2 – Reporting timeline requirements (not these alert clocks)

---

# Lesson 1.5.1 – Report Types

Source: `modules/01-soc/05-reporting/01-report-types/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 2b / 3c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the three kinds of report: **incident report**, **RFI**, and **other** as your shop uses it.
2. Given a situation, pick the type and say why it is not the **adjacent** type.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

---

## 1. Key Concepts

After you decide an alert is a case, or that you need another desk's help, you pick the **kind of record**. The next desk needs a **case** or a **question**, not both mixed in one product. That is the job in this lesson: name the type first, and say why the next-closest wrong type is wrong. That next-closest wrong type is the **adjacent** type (the **neighbor**).

| Type | What it is | Next-closest wrong type |
|------|------------|-------------------------|
| **Incident report** | Records a security incident (or a strongly supported suspected one) that needs a case / IR handoff | **RFI** — you already have enough to record the case; asking a question is a different product |
| **RFI** (Request for Information) | Asks another desk (CTI, hunt, IT, a vendor) for information so you can continue | **Incident** — an RFI can sit **beside** a case; it is the question, not a second case record |
| **Other (your shop)** | A name your site already uses | Say the local name and which neighbor you rejected. Do not invent a type. Do not park a finished intel paper here (**2.11**) |

The pair that gets mixed up is **incident ↔ RFI**. An RFI can sit beside an incident. It is not a second case. The RFI is the door into CTI.

**What good looks like:** two sentences — the **type**, and **not the neighbor because …**. You do not write the body yet.

- **Incident, not RFI:** First record for **A12** — `WS-JLEE` / `jlee`, `wscript` → `-enc`, Temp `invoice.vbs`. Type **incident report**. Not RFI: you are recording the case for IR, not asking a question. (A later RFI on the domain is a second product.)
- **RFI, not incident:** **A12** already exists. You want CTI to work the update domain / file. Type **RFI**. Not incident: the case is already open; this product is the question.

Do not invent a type list for this course's company. If you need **other**, use a name your real shop already has.

This lesson only names the type. Due clocks are **1.5.2**. Recipients and channel are **1.5.3**.

---

## 2. Knowledge Check

1. An RFI is a second incident case. True or false?
2. What is an incident report for, versus an RFI?
3. **A12** already exists. You want CTI to work the update domain. Type, and why not the adjacent one?

---

## 3. Summary

An incident report records the case. An RFI asks a question — and is the door into CTI. Other is a name your shop already uses. Name the type and reject the neighbor.

**Next:** **1.5.2** Reporting timeline requirements.

---

## 4. Related modules

- 1.4.5 – SLA / response time goals (previous — alert clocks, not report clocks)
- 1.5.2 – Reporting timeline requirements
- 1.5.3 – Notification and distribution
- 2.11 – Intelligence production (not a 1.5 type)

---

# Lesson 1.5.2 – Reporting Timeline Requirements

Source: `modules/01-soc/05-reporting/02-reporting-timelines/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 A / B / B ; 1.5.2.2 2b / 3c / 4c  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the two kinds of report clock: **submit** (by type) and **escalate-for-more-info**.
2. Given timestamps, say **which clock applies** and whether it is **at risk**.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Reporting timeline requirements
- T: 1.5.2.2 – Given timestamps, identify which report timeline applies and whether it is at risk

---

## 1. Key Concepts

SOC analysts watch **report** clocks so a case record and a CTI question leave the desk on time, and so a blocker is escalated instead of sitting. **1.5.1** already named the type — **incident report** (the case record) or **RFI** (the question to another desk). This lesson is **which clock** applies to that type, and whether it is **at risk**. It is **not** the alert 15 / 45 clocks (**1.4.5**). It is **not** who gets the report (**1.5.3**).

**Classroom numbers (this lesson only — not a live shop policy):**

| Clock | From | Classroom |
|-------|------|-----------|
| **Submit — incident** | Decision that an **incident report** is required | **30 minutes** |
| **Submit — RFI** | The **question** arises | **60 minutes** |
| **Escalate-for-more-info** | You become **blocked** (cannot finish without another desk) | **15 minutes** |

If your shop uses different minutes, use those. The obligation is **submit-by-type** plus **blocked → escalate**, not 30 / 60 / 15. If your shop has an **other** type, that type has its own submit number — do not invent one here.

**At risk** means the named clock will miss if you wait, or it is already past. “Late” with no clock name is not the task.

Two clocks can be live. When you are blocked, name **escalate-for-more-info** first. Submit is still running.

**What good looks like:**

- **Submit — RFI, at risk:** **A12** exists. Question to CTI on the update domain at `13:30`. Still unsent. Now `14:40`. Clock: **submit — RFI** (70 minutes, past 60). Not the 30-minute incident clock. Not the alert-close clock.
- **Escalate-for-more-info, at risk:** **A12** incident decision `14:00`. At `14:10` you cannot finish without another desk. Still blocked. Now `14:28`. Clock: **escalate-for-more-info** (18 minutes, past 15). Submit-incident is still running (28 of 30) — act on the blocker.

---

## 2. Knowledge Check

1. This lesson uses the same 15 / 45 clocks as **1.4.5**. True or false?
2. When does the **escalate-for-more-info** clock start?
3. RFI question at `13:30`, still unsent at `14:40`. Which clock, and is it at risk?

---

## 3. Summary

Submit by type. When blocked, escalate. Name the clock. These are not the alert SLA clocks.

**Next:** **1.5.3** Notification and distribution.

---

## 4. Related modules

- 1.5.1 – Report types (previous)
- 1.5.3 – Notification and distribution
- 1.4.5 – SLA / response time goals (alert clocks, not these)

---

# Lesson 1.5.3 – Notification and Distribution

Source: `modules/01-soc/05-reporting/03-notification-distribution/student-guide.md`

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B ; 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a notification chart: **who** receives the report, whether **leadership** gets awareness, and which **channel** is approved.
2. Route a report: name recipients, whether leadership gets awareness, the approved channel, and **reject the wrong channel**.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

---

## 1. Key Concepts

SOC analysts put the case record and the CTI question on an **approved path** so IR and leadership actually see them. An incident that only lives in a private chat is not a handoff. An RFI sent as a text is not a request the CTI desk can work. **1.5.1** named the type. **1.5.2** named the clock. This lesson is **who** receives the report, whether **leadership** gets awareness, and **which channel** is approved. You do **not** pick the type again. You do **not** score the 30 / 60. You do **not** write the body. **1.7** is retired — it is not a 1.5 channel.

A **notification chart** (sometimes called a **matrix**) is a table that says which teams receive which report type, whether leadership gets awareness, and which channel is approved.

**Classroom chart (this lesson only — not a live shop matrix):**

| Type | Recipients | Leadership awareness | Approved channel |
|------|------------|----------------------|------------------|
| **Incident** | SOC queue + **IR** | **Yes** — duty SOC lead | **Ticket** (the case system) |
| **RFI** | The **named team** (CTI, hunt, or IT) | **No**, unless they asked or the chart says so | **Ticket** or **approved RFI form** |

If your shop has a real chart, use it. The obligation is **who + leadership yes/no + approved channel**, not these names. If your shop has an **other** type, it has its own row — do not invent one here.

**Leadership awareness** is a yes or no on the chart. It is not “email the CEO.” The duty SOC lead counts. The leadership product is a short awareness flag, not the file hash.

**Approved** (classroom): ticket, approved RFI form.  
**Not approved** (classroom): personal SMS, private chat, personal mail off-domain.

Right people on the **wrong path** still fails.

The route is four facts: **recipients**, **leadership yes/no**, **channel**, **rejected channel**.

**What good looks like:**

- **Incident, ticket:** First IR handoff for **A12** (`WS-JLEE` / `jlee`, `wscript` → `-enc`, Temp `invoice.vbs`). Recipients **SOC + IR**. Leadership **yes**. Channel **ticket**. Reject: personal email or chat to the IR analyst only.
- **RFI, not SMS:** **A12** exists. Ask CTI to work the update domain. Recipients **CTI**. Leadership **no**. Channel **ticket or RFI form**. Reject: texting a CTI friend. Right team, wrong path.

---

## 2. Knowledge Check

1. This lesson is when the report is due. True or false?
2. What three things does the notification chart tell you?
3. First IR handoff for **A12**. Recipients, leadership yes/no, channel, and one rejected channel?

---

## 3. Summary

The chart names who, leadership, and channel. Reject the unofficial path. This closes **1.5**. SOC reporting ends here.

**Next:** **2.1.1** Data, information, and intelligence. The RFI is the door into CTI.

---

## 4. Related modules

- 1.5.2 – Reporting timeline requirements (previous)
- 1.5.1 – Report types
- 2.1.1 – Data, information, and intelligence
- 2.11 – Intelligence production (not a 1.5 route)
