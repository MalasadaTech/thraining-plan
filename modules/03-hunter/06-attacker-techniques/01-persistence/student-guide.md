# Module 3.6.1 – Persistence Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.1 B / C / C ; 3.6.1.1 3c / 4c / 4c  
- SOC: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
- CTI: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Recognize common Windows persistence mechanisms in host telemetry.
2. Identify the fields that demonstrate the mechanism while separating **technique recognition** from a judgment that the activity is malicious.

## Mapped Proficiency Items

- K: 3.6.1 – Persistence techniques
- T: 3.6.1.1 – Recognize persistence techniques in logs or telemetry

## 1. Key Concepts

Persistence is how an adversary maintains access or recurring execution across interruptions such as logon, reboot, process termination, or other changes in session state.

This lesson focuses on several Windows mechanisms hunters commonly encounter.

### Registry Run keys and Startup Folder

MITRE ATT&CK: [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)

Useful evidence includes:

- exact registry path;
- value name;
- value data/target path;
- process/user that created or modified it;
- file metadata for the target.

A12:

> `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`  
> `Updater = %TEMP%\update.exe`

That supports **user-context persistence** because Windows can execute the referenced program at logon.

It does not, by itself, establish privilege escalation.

### Scheduled Tasks

MITRE ATT&CK: [T1053.005 – Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)

Useful evidence includes:

- task name/path;
- trigger;
- action/command;
- principal/account;
- creator/modifier;
- creation/update time.

A scheduled task can be used for **Execution, Persistence, or Privilege Escalation** depending on how it is configured and used. Classification should follow the observed role.

### Windows Services

MITRE ATT&CK: [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)

Useful evidence includes:

- service name;
- image path;
- start type;
- service account;
- creator/modifier;
- whether the binary/path is expected.

Services can support persistence and can also result in elevated execution when the necessary prerequisites are present.

### Other recurring mechanisms

Examples include:

- WMI event subscriptions;
- logon scripts;
- Winlogon modifications;
- other boot/logon autostart locations.

Name the mechanism the telemetry supports rather than forcing every recurring execution into “Run key.”

### Recognizing a technique does not mean declaring malware

Legitimate software uses persistence mechanisms every day.

A vendor updater in a known path can legitimately create an autorun.

Hunting asks what makes the instance suspicious:
- unusual creator;
- user-writable target;
- rare value/task/service name;
- unsigned or unexpected binary;
- timing around an incident;
- unexpected account or host population.

## 2. Knowledge Check

1. What fields make a Run-key persistence observation reviewable?
2. Why can a scheduled task map to more than one ATT&CK tactic?
3. Does a legitimate updater that creates a Run key stop being a persistence mechanism? Explain.

## 3. Summary

Recognize the mechanism first; judge suspiciousness second.

Registry autoruns, Startup folders, scheduled tasks, services, and other recurring mechanisms all need the fields that show **what will run, when, and under which context**.

**Next:** **3.6.2 – Privilege Escalation Techniques**.

## Supporting References

- [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
- [T1053.005 – Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)
- [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)
