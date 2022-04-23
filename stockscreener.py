# import required libraries
import yfinance as yf
import numpy as np
import pandas as pd


def rsi(df, periods=14, ema=True):
    """
    Returns a pd.Series with the relative strength index.
    """
    close_delta = df['Close'].diff()

    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    if ema == True:
        # Use exponential moving average
        ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    else:
        # Use simple moving average
        ma_up = up.rolling(window=periods, adjust=False).mean()
        ma_down = down.rolling(window=periods, adjust=False).mean()

    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    return rsi


stocks_SBF120 = ["AC.PA",
                 "ADP.PA", "AF.PA", "AI.PA", "ALO.PA", "ATE.PA",
                 "MT.PA", "AKE.PA", "ATO.PA", "CS.PA", "BEN.PA", "BB.PA", "BNP.PA",
                 "BON.PA", "EN.PA", "BVI.PA", "CAP.PA", "CA.PA", "CO.PA",
                 "CU.PA", "CNP.PA", "ACA.PA", "BN.PA", "DSY.PA", "DBG.PA", "DEXB.PA", "EAD.PA", "EDF.PA", "EEN.PA",
                 "FGR.PA", "ERA.PA", "EI.PA", "ELE.PA", "RF.PA", "ERF.PA", "ETL.PA", "FIM.PA", "FDR.PA", "FTE.PA",
                 "GSZ.PA", "GFC.PA", "GTO.PA", "GET.PA", "RIA.PA", "HAV.PA", "RMS.PA", "ICAD.PA", "ILD.PA", "NK.PA",
                 "IMS.PA", "ING.PA", "IPN.PA", "IPS.PA", "DEC.PA", "LI.PA", "OR.PA", "LG.PA", "MMB.PA", "LR.PA",
                 "MC.PA", "MAU.PA", "MMT.PA", "ML.PA", "KN.PA", "NEO.PA", "NEX.PA", "NXI.PA", "COX.PA", "ORP.PA",
                 "PAJ.PA", "RI.PA", "UG.PA", "PP.PA", "PUB.PA", "RCO.PA", "RNO.PA", "RXL.PA", "RHA.PA", "SK.PA",
                 "SAF.PA", "SAFT.PA", "SGO.PA", "SAN.PA", "SU.PA", "SCR.PA", "SCHP.PA", "SECH.PA", "SESG.PA", "SIL.PA",
                 "GLE.PA", "SW.PA", "SOI.PA", "SPR.PA", "GENP.PA", "STM.PA", "SEV.PA", "TEC.PA", "RCF.PA", "TFI.PA",
                 "HO.PA", "TMS.PA", "FP.PA", "UBI.PA", "UL.PA", "FR.PA", "VK.PA", "VIE.PA", "RIN.PA", "DG.PA", "VIV.PA",
                 "MF.PA", "ZC.PA"]

stocks_cac40 = ["AC.PA", "AI.PA", "ALU.PA", "ALO.PA", "MT.PA", "CS.PA", "BNP.PA", "EN.PA", "CAP.PA", "CA.PA", "ACA.PA",
                "BN.PA", "DEXB.PA", "EAD.PA", "EDF.PA", "EI.PA", "FTE.PA", "GSZ.PA", "OR.PA", "LG.PA", "LR.PA",
                "MMB.PA", "MC.PA", "ML.PA", "RI.PA", "UG.PA", "PP.PA", "RNO.PA", "SGO.PA", "SAN.PA",
                "SU.PA", "GLE.PA", "STM.PA", "TEC.PA", "FP.PA", "UL.PA", "VK.PA", "VIE.PA", "DG.PA", "VIV.PA"]

cac40_stocks = []
cac40_stocks_sector = []
cac40_stocks_RSI = []


for s in stocks_cac40:
    try:
        msft = yf.Ticker(s)
        hist = msft.history(period="30d")
        rsi_stock = list(rsi(hist))[-1]
        info = msft.get_info()['sector']
        cac40_stocks.append(s)
        cac40_stocks_sector.append(info)
        cac40_stocks_RSI.append(round(rsi_stock, 1))
    except:
        pass

df = pd.DataFrame.from_dict({"Stock name": cac40_stocks, "Sector": cac40_stocks_sector, "RSI": cac40_stocks_RSI})
df.to_csv("./data/stocks_cac40.csv")

cac40_stocks = []
cac40_stocks_sector = []
cac40_stocks_RSI = []

for s in stocks_SBF120:
    try:
        msft = yf.Ticker(s)
        hist = msft.history(period="30d")
        rsi_stock = list(rsi(hist))[-1]
        info = msft.get_info()['sector']
        cac40_stocks.append(s)
        cac40_stocks_sector.append(info)
        cac40_stocks_RSI.append(round(rsi_stock, 1))
    except:
        pass

df = pd.DataFrame.from_dict({"Stock name": cac40_stocks, "Sector": cac40_stocks_sector, "RSI": cac40_stocks_RSI})
df.to_csv("./data/stocks_sbf120.csv")