# Structural Number System – MVP

This repository contains a minimal runnable implementation of the **Structural Number System** (part of *Meta‑Core Theory*).

## 📘 Core idea
Each semantic unit is expressed as:

```
(value, is_focused)
```

* `value` – the numerical/content part  
* `is_focused` – whether this content is currently **in focus / 显现**  

This separates **存在/显现** from **值内容**, solving classic ambiguities such as:

* “一个零到底是一还是零？”
* Distinguishing `NULL` vs `0`
* Negation vs absence in NLP

## 📂 Quick start

```bash
python demo/coin_example.py
```

Expected output:

```
coin1: (0, True)
coin2: (0, False)
coin3: (1, True)
coin4: (1, False)

Classical   sum(value)             = 2
Structural  sum(structural_amount) = 1
Focus count  (how many in focus)   = 2
```

## 🧠 Credits
Proposed by **Meta‑Core Theory (元核论)**. Code prepared via ChatGPT for user *Lai012345*.
