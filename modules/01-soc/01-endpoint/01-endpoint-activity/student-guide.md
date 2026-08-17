# Module 1.1.1 – Endpoint activity (the map)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the five kinds of **host rows** this unit will teach.
2. Given a one-line description, say whether it is **process**, **file**, **registry**, **host-network**, or **image/driver load**.

**Mapped Proficiency Items:**
- K: 1.1.1.1 – Endpoint activity (the map)
- T: 1.1.1.2 – Given a one-line description, name the activity type

---

## 1. Key Concepts

An alert will point at a **host**. Before you describe a row, you need to know **which kind of row** you are looking at. This hour is that map.

A host leaves **rows** when something happens on it:

| Kind | What happened |
|------|----------------|
| **Process** | A program ran, ended, or touched another program |
| **File** | A file was created, moved, changed, read, or deleted |
| **Registry** | A key or value was set, deleted, or renamed |
| **Host-network** | This host talked (IP, port, domain) — the *process* started it |
| **Image / driver load** | A DLL or driver was loaded |

**Sysmon** and **MDE** are two encodings of those **same** activities, not two different stories. This course uses both as examples. This is **not** how to install Sysmon.

You will learn **one activity type at a time** after this hour. This hour is only the map.

This is **endpoint** telemetry. Protocol deep-dive is Zeek (**1.2**).

**What good looks like:** someone gives you one line. You name the kind. You do not describe fields yet.

- Given: “A program started on the host.” **Process.**
- Given: “A file appeared in Temp.” **File.**
- Given: “This host connected to an IP and port.” **Host-network.**

Do not tell the rest of the incident. Do not open a process row yet (**1.1.2**).

---

## 2. Knowledge Check

1. Sysmon and MDE are two different stories. True or false?
2. “A program started on the host.” Which activity type is that?
3. “This host connected to an IP and port.” Process, or host-network?

---

## 3. Summary

Five kinds of host rows. Sysmon and MDE encode the same activities. Know the kind before you describe the row. Zeek is later.

**Next:** **1.1.2** Process activity.

---

## 4. Related modules

- 0.5 – How this course is laid out
- 1.1.2 – Process activity
- 1.2 – Zeek
