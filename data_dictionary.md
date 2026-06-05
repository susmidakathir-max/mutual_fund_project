\# Data Dictionary



\## Fund Master (01\_fund\_master.csv)



| Column       | Data Type | Description             |

| ------------ | --------- | ----------------------- |

| amfi\_code    | Integer   | Unique AMFI scheme code |

| fund\_house   | Text      | Mutual fund company     |

| scheme\_name  | Text      | Name of scheme          |

| category     | Text      | Fund category           |

| sub\_category | Text      | Detailed category       |



\## NAV History (02\_nav\_history.csv)



| Column    | Data Type | Description      |

| --------- | --------- | ---------------- |

| amfi\_code | Integer   | AMFI scheme code |

| date      | Date      | NAV date         |

| nav       | Decimal   | Net Asset Value  |



\## Investor Transactions (08\_investor\_transactions.csv)



| Column           | Data Type | Description                |

| ---------------- | --------- | -------------------------- |

| investor\_id      | Text      | Investor identifier        |

| transaction\_date | Date      | Transaction date           |

| amfi\_code        | Integer   | Scheme code                |

| transaction\_type | Text      | SIP, Lumpsum or Redemption |

| amount\_inr       | Decimal   | Transaction amount         |

| state            | Text      | Investor state             |

| city             | Text      | Investor city              |

| kyc\_status       | Text      | KYC verification status    |



\## Scheme Performance (07\_scheme\_performance.csv)



| Column            | Data Type | Description              |

| ----------------- | --------- | ------------------------ |

| amfi\_code         | Integer   | Scheme code              |

| return\_1yr\_pct    | Decimal   | 1-year return percentage |

| return\_3yr\_pct    | Decimal   | 3-year return percentage |

| return\_5yr\_pct    | Decimal   | 5-year return percentage |

| expense\_ratio\_pct | Decimal   | Expense ratio percentage |

| risk\_grade        | Text      | Risk category            |



Source: Bluestock Mutual Fund Analytics Project Datasets



