# SEBI registered intermediary database and scam alerts

sebi_intermediaries = [
    # Registered Investment Advisers (RIA)
    {"name": "Priya Sharma Financial Advisory", "reg_number": "INA000012345", "category": "Investment Adviser", "status": "Active", "city": "Mumbai", "reg_date": "2018-03-15"},
    {"name": "Karthik Rangappa Wealth", "reg_number": "INA000006789", "category": "Investment Adviser", "status": "Active", "city": "Bangalore", "reg_date": "2017-06-22"},
    {"name": "Pattu Investments", "reg_number": "INA000008901", "category": "Investment Adviser", "status": "Active", "city": "Chennai", "reg_date": "2019-01-10"},
    {"name": "Capital Mind Financial Services", "reg_number": "INA000002345", "category": "Investment Adviser", "status": "Active", "city": "Bangalore", "reg_date": "2016-09-05"},
    {"name": "Ravi Saraogi Advisory", "reg_number": "INA000011234", "category": "Investment Adviser", "status": "Active", "city": "Kolkata", "reg_date": "2020-04-18"},
    {"name": "NiveshPath Advisors", "reg_number": "INA000013456", "category": "Investment Adviser", "status": "Active", "city": "Delhi", "reg_date": "2021-02-28"},
    {"name": "FinPlan India Advisors", "reg_number": "INA000014567", "category": "Investment Adviser", "status": "Active", "city": "Pune", "reg_date": "2019-07-12"},
    {"name": "Arjun Desai Wealth", "reg_number": "INA000015678", "category": "Investment Adviser", "status": "Suspended", "city": "Ahmedabad", "reg_date": "2017-11-30"},
    {"name": "Meera Patel Advisory", "reg_number": "INA000016789", "category": "Investment Adviser", "status": "Active", "city": "Mumbai", "reg_date": "2022-05-14"},
    {"name": "WealthFirst Advisors", "reg_number": "INA000017890", "category": "Investment Adviser", "status": "Active", "city": "Hyderabad", "reg_date": "2020-08-20"},
    # Research Analysts (RA)
    {"name": "MarketPulse Research", "reg_number": "INH000004567", "category": "Research Analyst", "status": "Active", "city": "Mumbai", "reg_date": "2018-11-01"},
    {"name": "StockEdge Research Services", "reg_number": "INH000005678", "category": "Research Analyst", "status": "Active", "city": "Delhi", "reg_date": "2017-03-20"},
    {"name": "Equitymaster Research", "reg_number": "INH000006789", "category": "Research Analyst", "status": "Active", "city": "Mumbai", "reg_date": "2015-06-15"},
    {"name": "Moneycontrol Research", "reg_number": "INH000007890", "category": "Research Analyst", "status": "Active", "city": "Mumbai", "reg_date": "2016-01-10"},
    {"name": "IIFL Research", "reg_number": "INH000008901", "category": "Research Analyst", "status": "Active", "city": "Mumbai", "reg_date": "2014-09-25"},
    # Stock Brokers
    {"name": "Zerodha Broking Ltd", "reg_number": "INZ000031633", "category": "Stock Broker", "status": "Active", "city": "Bangalore", "reg_date": "2010-08-15"},
    {"name": "Groww (Billionbrains)", "reg_number": "INZ000313732", "category": "Stock Broker", "status": "Active", "city": "Bangalore", "reg_date": "2018-04-10"},
    {"name": "Angel One Ltd", "reg_number": "INZ000078437", "category": "Stock Broker", "status": "Active", "city": "Mumbai", "reg_date": "2007-12-20"},
    {"name": "Upstox (RKSV Securities)", "reg_number": "INZ000185137", "category": "Stock Broker", "status": "Active", "city": "Mumbai", "reg_date": "2012-05-30"},
    {"name": "ICICI Securities Ltd", "reg_number": "INZ000183631", "category": "Stock Broker", "status": "Active", "city": "Mumbai", "reg_date": "2000-03-14"},
    {"name": "HDFC Securities Ltd", "reg_number": "INZ000186937", "category": "Stock Broker", "status": "Active", "city": "Mumbai", "reg_date": "2000-06-22"},
    {"name": "Kotak Securities Ltd", "reg_number": "INZ000200137", "category": "Stock Broker", "status": "Active", "city": "Mumbai", "reg_date": "1994-12-01"},
    {"name": "Motilal Oswal Financial Services", "reg_number": "INZ000158036", "category": "Stock Broker", "status": "Active", "city": "Mumbai", "reg_date": "2005-07-18"},
    # Portfolio Managers
    {"name": "Marcellus Investment Managers", "reg_number": "INP000005786", "category": "Portfolio Manager", "status": "Active", "city": "Mumbai", "reg_date": "2018-10-12"},
    {"name": "Avendus Capital PMS", "reg_number": "INP000004521", "category": "Portfolio Manager", "status": "Active", "city": "Mumbai", "reg_date": "2016-02-08"},
    {"name": "ASK Investment Managers", "reg_number": "INP000003267", "category": "Portfolio Manager", "status": "Active", "city": "Mumbai", "reg_date": "2012-08-20"},
    # MF Distributors
    {"name": "NJ Wealth (NJ India Invest)", "reg_number": "ARN-0002", "category": "MF Distributor", "status": "Active", "city": "Surat", "reg_date": "2003-04-15"},
    {"name": "Prudent Corporate Advisory", "reg_number": "ARN-0035", "category": "MF Distributor", "status": "Active", "city": "Ahmedabad", "reg_date": "2005-11-20"},
    {"name": "Anand Rathi Wealth Services", "reg_number": "ARN-0048", "category": "MF Distributor", "status": "Active", "city": "Mumbai", "reg_date": "2002-09-10"},
    # Depository Participants
    {"name": "CDSL (Central Depository Services)", "reg_number": "IN-DP-CDSL-00001", "category": "Depository Participant", "status": "Active", "city": "Mumbai", "reg_date": "1999-02-15"},
    {"name": "NSDL (National Securities Depository)", "reg_number": "IN-DP-NSDL-00001", "category": "Depository Participant", "status": "Active", "city": "Mumbai", "reg_date": "1996-11-08"},
]

scam_alerts = [
    {"id": "SCAM-001", "scheme_name": "QuickProfit Trading Academy", "alert_date": "2025-12-10", "type": "Unregistered Investment Adviser", "description": "Operating Telegram channels providing stock tips and charging fees without SEBI registration. Claims guaranteed 50% monthly returns.", "sebi_order_ref": "WTM/AB/MIRSD/2025/001", "risk_level": "High", "keywords": ["quickprofit", "quick profit", "trading academy"]},
    {"id": "SCAM-002", "scheme_name": "GoldMine Crypto Invest", "alert_date": "2025-11-22", "type": "Ponzi Scheme", "description": "Promising 200% returns through crypto-gold hybrid investments. No underlying assets. Operating through WhatsApp groups.", "sebi_order_ref": "WTM/CD/MIRSD/2025/042", "risk_level": "Critical", "keywords": ["goldmine", "crypto invest", "gold mine crypto"]},
    {"id": "SCAM-003", "scheme_name": "StockKing Pro Tips", "alert_date": "2026-01-15", "type": "Unregistered Research Analyst", "description": "YouTube channel with 500K subscribers providing 'guaranteed intraday tips' for ₹999/month subscription. Not registered with SEBI as RA.", "sebi_order_ref": "WTM/EF/MIRSD/2026/003", "risk_level": "High", "keywords": ["stockking", "stock king", "pro tips"]},
    {"id": "SCAM-004", "scheme_name": "SafeReturn Fixed Deposit Plus", "alert_date": "2025-10-05", "type": "Collective Investment Scheme", "description": "Collecting deposits from public promising 18% fixed returns. Not registered as NBFC or with SEBI.", "sebi_order_ref": "WTM/GH/CIS/2025/089", "risk_level": "Critical", "keywords": ["safereturn", "safe return", "fd plus", "fixed deposit plus"]},
    {"id": "SCAM-005", "scheme_name": "WealthWizard AI Trading Bot", "alert_date": "2026-02-20", "type": "Unregistered Investment Adviser", "description": "Selling an 'AI-powered trading bot' that auto-trades on user's demat account. Charges ₹50,000 upfront + 30% profit share. No SEBI registration.", "sebi_order_ref": "WTM/IJ/MIRSD/2026/015", "risk_level": "High", "keywords": ["wealthwizard", "wealth wizard", "ai trading bot"]},
    {"id": "SCAM-006", "scheme_name": "ProfitMatrix Options Mentorship", "alert_date": "2026-03-08", "type": "Unregistered Research Analyst", "description": "Instagram influencer selling F&O 'mentorship' course with live trading calls. No RA registration.", "sebi_order_ref": "WTM/KL/MIRSD/2026/022", "risk_level": "High", "keywords": ["profitmatrix", "profit matrix", "options mentorship"]},
    {"id": "SCAM-007", "scheme_name": "BharatWealth Chit Fund", "alert_date": "2025-09-18", "type": "Collective Investment Scheme", "description": "Running unregistered chit fund scheme collecting monthly contributions across Karnataka and Tamil Nadu.", "sebi_order_ref": "WTM/MN/CIS/2025/056", "risk_level": "Critical", "keywords": ["bharatwealth", "bharat wealth", "chit fund"]},
    {"id": "SCAM-008", "scheme_name": "NiftyGains Premium Telegram", "alert_date": "2026-04-12", "type": "Unregistered Investment Adviser", "description": "Premium Telegram group charging ₹15,000/quarter for Nifty/BankNifty options calls. Claims 90% accuracy. Zero SEBI registration.", "sebi_order_ref": "WTM/OP/MIRSD/2026/031", "risk_level": "High", "keywords": ["niftygains", "nifty gains", "premium telegram"]},
    {"id": "SCAM-009", "scheme_name": "EasyMoney Forex Academy", "alert_date": "2026-01-30", "type": "Unregistered Investment Adviser", "description": "Offering forex trading courses and managed accounts via Instagram reels targeting college students.", "sebi_order_ref": "WTM/QR/MIRSD/2026/008", "risk_level": "High", "keywords": ["easymoney", "easy money", "forex academy"]},
    {"id": "SCAM-010", "scheme_name": "Digital Rupee Invest", "alert_date": "2025-08-25", "type": "Ponzi Scheme", "description": "Falsely claiming association with RBI Digital Rupee. Collecting investments in a fake 'digital rupee staking' program.", "sebi_order_ref": "WTM/ST/CIS/2025/072", "risk_level": "Critical", "keywords": ["digital rupee invest", "digital rupee staking"]},
    {"id": "SCAM-011", "scheme_name": "MasterTrader FnO Signals", "alert_date": "2026-05-05", "type": "Unregistered Research Analyst", "description": "Providing F&O trading signals via WhatsApp for ₹5,000/month. No SEBI RA registration.", "sebi_order_ref": "WTM/UV/MIRSD/2026/044", "risk_level": "High", "keywords": ["mastertrader", "master trader", "fno signals"]},
    {"id": "SCAM-012", "scheme_name": "GreenEnergy Returns Ltd", "alert_date": "2026-02-14", "type": "Collective Investment Scheme", "description": "Promising 24% annual returns through 'solar farm investments'. Not registered with SEBI.", "sebi_order_ref": "WTM/WX/CIS/2026/018", "risk_level": "Critical", "keywords": ["greenenergy", "green energy returns", "solar investment"]},
]

known_finfluencers = [
    {"name": "FinanceGuru_YT", "platform": "YouTube", "followers": "1.2M", "sebi_registered": False, "risk_flag": True},
    {"name": "StockSensei_Insta", "platform": "Instagram", "followers": "800K", "sebi_registered": False, "risk_flag": True},
    {"name": "CryptoKing_Telegram", "platform": "Telegram", "followers": "350K", "sebi_registered": False, "risk_flag": True},
    {"name": "MutualFundSahi", "platform": "YouTube", "followers": "2.1M", "sebi_registered": False, "risk_flag": False},
    {"name": "OptionsBaba", "platform": "Telegram", "followers": "450K", "sebi_registered": False, "risk_flag": True},
    {"name": "WealthCoach_Ram", "platform": "Instagram", "followers": "650K", "sebi_registered": False, "risk_flag": True},
]
