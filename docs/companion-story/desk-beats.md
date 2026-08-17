# Desk beats

Instructor card. Same facts as the [story bible](../story-bible.md) “when each fact appears” table. Use this when a lesson starts dumping the whole chain.

| Fact | First plant | First use in the flow | Do not dump it in |
|------|-------------|-----------------------|-------------------|
| `wscript` → `powershell -enc` on **WS-JLEE** / `jlee` | **1.1.2** process | **1.4** the alert (what fired) | — |
| `invoice.vbs` in Temp | **1.1.3** file | **1.4.1** investigation; **1.5** notify (path, not hash) | Leadership one-liner does not need the hash |
| SOC VT lookup of a hash, IP, or domain they already have | **0.7** survey | **1.4.1** first pass — here, the `invoice.vbs` hash | Relations tab; a detection count as a hunt |
| HKCU Run **`Updater`** → `%TEMP%\update.exe` | **1.1.5** registry | **3.x** hunt (more hosts) | First alert. Leadership notify |
| Host GET `update.exe` `:8080` to `prd-updates.net` / `203.0.113.88` | **1.1.4** + **1.2** Zeek | **1.4.1** if they pull PCAP/Zeek; **2.11.3** RFI seed | Not all of this in the leadership notify |
| FN: that GET with **no** queue row | **1.4.2** | Hunt purpose **3.1**; DE gap **4.5** | Calling FN a disliked TP |
| Sibling `login-prd.net`, same NS, same A | **2.5** / **2.6** / **2.8** | Extra infra → **block** (0.3 e) | SOC notify field |
| Hunt package: `Updater` / `update.exe` / more `invoice.vbs` | **3.x** | Hunt product; same package to **4.x** | Rewrite of the SOC ticket |
| Nomination / add / no new rule | **4.3** / **4.5** | After the hunt or SOC “we keep missing this” | Invented in 1.1; used as a block list |

## Products (do not collapse)

| Product | Owner | Not |
|---------|-------|-----|
| Queue investigation + TP/FN cite | SOC **1.4** | A hunt card |
| Incident + leadership one-liner | SOC **1.5** | The RFI answer |
| RFI answer | CTI **2.11.3** | A second incident |
| Hop sentence | CTI **2.8.1** | A `/24` |
| Block / blacklist | Firewall / IA | A DE deploy |
| Hunt package | Hunt **3.x** | A rewritten ticket; Hunt-17 |
| Nomination review | DE **4.3** / **4.5** | The rule text (**1.3**) |

## Not in A12

OT, `pay-db-01`, vendor VPN, `checkin` / beacon POST, `helpdesk.exe`, Word → `helper.dll`. Extra example rows may reuse `jlee` / **WS-JLEE**. They are not this plot.
