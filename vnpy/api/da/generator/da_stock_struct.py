CStockRspInfoField = {
    "ErrorID": "int",
    "ErrorMsg": "string",
}

CStockReqUserLoginField = {
    "UserId": "string",
    "UserPwd": "string",
    "UserType": "string",
    "MacAddress": "string",
    "ComputerName": "string",
    "SoftwareName": "string",
    "SoftwareVersion": "string",
    "AuthorCode": "string",
    "ErrorDescription": "string",
}

CStockRspAccountField = {
    "UserId": "string",
    "UserName": "string",
    "UserType": "string",
    "LoginPwd": "string",
    "AccountNo": "string",
    "TradePwd": "string",
    "IsSimulation": "string",
    "FrontendIp": "string",
    "FrontendPort": "string",
    "CurrencyNo": "string",
    "UserState": "string",
    "SelAll": "string",
    "Strategy": "string",
    "Inner": "string",
    "YingSun": "string",
    "ChaoDan": "string",
    "Option": "string",
    "CmeMarket": "string",
    "CmeCOMEXMarket": "string",
    "CmeNYMEXMarket": "string",
    "CmeCBTMarket": "string",
    "IceUSMarket": "string",
    "IceECMarket": "string",
    "IceEFMarket": "string",
    "CanTradeStockHK": "string",
    "CanTradeStockAM": "string",
    "MultiLogin": "string",
    "SellStockHK": "string",
    "SellStockAM": "string",
    "CanTradeStockKRX": "string",
    "HkexMarket": "string",
    "IdNumber": "string",
    "HkexMarketFee": "string",
    "IsProfessional": "string",
    "IsOverSea": "string",
    "IsFirstLogin": "string",
    "UserMobile": "string",
    "HasSetQA": "string",
    "CanTradeStockSGXQ": "string",
    "ExistMac": "string",
    "RatioINE": "string",
    "EurexMarket": "string",
    "HkexIsOverMaxTerminal": "string",
    "HkexOverMoney": "string",
    "CanTradeStockAU": "string",
    "NyFlag": "string",
}

CStockReqUserLogoutField = {
    "UserId": "string",
    "AccountNo": "string",
    "ErrorDescription": "string",
}

CStockReqOrderInsertField = {
    "UserId": "string",
    "UserType": "string",
    "AccountNo": "string",
    "LocalNo": "string",
    "TradePwd": "string",
    "IsRiskOrder": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "AddReduce": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "TradeType": "string",
    "PriceType": "string",
    "HtsType": "string",
    "ForceID": "string",
    "TriggerPrice": "string",
    "ValidDate": "string",
    "StrategyId": "string",
    "MaxShow": "string",
    "MinQty": "string",
    "ErrorDescription": "string",
}

CStockRspOrderInsertField = {
    "UserId": "string",
    "AccountNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "OrderNo": "string",
    "OrigOrderNo": "string",
    "OrderMethod": "string",
    "AcceptType": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "FilledNumber": "string",
    "FilledPrice": "string",
    "TradeType": "string",
    "PriceType": "string",
    "HtsType": "string",
    "OrderDate": "string",
    "OrderTime": "string",
    "ErrorCode": "string",
    "OrderState": "string",
    "IsRiskOrder": "string",
    "CancelUserId": "string",
    "TriggerPrice": "string",
    "ValidDate": "string",
    "AddReduce": "string",
    "StrategyId": "string",
    "MaxShow": "string",
    "MinQty": "string",
    "ExchangeTime": "string",
    "CancelTime": "string",
}

CStockReqOrderModifyField = {
    "SystemNo": "string",
    "UserId": "string",
    "UserType": "string",
    "LocalNo": "string",
    "AccountNo": "string",
    "TradePwd": "string",
    "OrderNo": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "FilledNumber": "string",
    "ModifyNumber": "string",
    "ModifyPrice": "string",
    "TradeType": "string",
    "PriceType": "string",
    "IsRiskOrder": "string",
    "TriggerPrice": "string",
    "ModifyTriggerPrice": "string",
    "ValidDate": "string",
    "ErrorDescription": "string",
}

CStockRspOrderModifyField = CStockRspOrderInsertField

CStockReqOrderCancelField = {
    "UserId": "string",
    "UserType": "string",
    "LocalNo": "string",
    "AccountNo": "string",
    "TradePwd": "string",
    "IsSimulation": "string",
    "SystemNo": "string",
    "OrderNo": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "FilledNumber": "string",
    "TradeType": "string",
    "PriceType": "string",
    "HtsType": "string",
    "IsRiskOrder": "string",
    "ErrorDescription": "string",
}

CStockRspOrderCancelField = {
    "UserId": "string",
    "AccountNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "OrderNo": "string",
    "CancelNo": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "FilledNumber": "string",
    "CancelNumber": "string",
    "TradeType": "string",
    "PriceType": "string",
    "HtsType": "string",
    "CancelDate": "string",
    "CancelTime": "string",
    "ErrorCode": "string",
    "IsRiskOrder": "string",
}

CStockReqPasswordUpdateField = {
    "UserId": "string",
    "OldPassword": "string",
    "NewPassword": "string",
    "ErrorDescription": "string",
}

CStockRspPasswordUpdateField = {
    "UserId": "string",
    "OldPassword": "string",
    "NewPassword": "string",
}

CStockQryOrderField = {
    "UserId": "string",
    "UserType": "string",
    "AccountNo": "string",
    "TradePwd": "string",
    "IsSimulation": "string",
    "OrderNo": "string",
    "OrderDateTime": "string",
    "ErrorDescription": "string",
}

CStockRspOrderField = {
    "UserId": "string",
    "AccountNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "OrderNo": "string",
    "OrigOrderNo": "string",
    "OrderMethod": "string",
    "AcceptType": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "FilledNumber": "string",
    "FilledPrice": "string",
    "TradeType": "string",
    "PriceType": "string",
    "HtsType": "string",
    "OrderDate": "string",
    "OrderTime": "string",
    "ErrorCode": "string",
    "OrderState": "string",
    "IsRiskOrder": "string",
    "CancelUserId": "string",
    "TriggerPrice": "string",
    "ValidDate": "string",
    "AddReduce": "string",
    "StrategyId": "string",
    "MaxShow": "string",
    "MinQty": "string",
    "ExchangeTime": "string",
    "CancelTime": "string",
}

CStockQryTradeField = {
    "UserId": "string",
    "ErrorDescription": "string",
}

CStockRspTradeField = {
    "UserId": "string",
    "AccountNo": "string",
    "FilledNo": "string",
    "OrderNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "FilledNumber": "string",
    "FilledPrice": "string",
    "FilledDate": "string",
    "FilledTime": "string",
    "Commsion": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "DeliveryDate": "string",
    "FilledType": "string",
    "OrderType": "string",
    "ValidDate": "string",
    "AddReduce": "string",
    "ErrorDescription": "string",
}

CStockQryInstrumentField = {
    "PageIndex": "int",
    "ExchangeNo": "string",
    "ErrorDescription": "string",
}

CStockRspInstrumentField = {
    "ExchangeNo": "string",
    "ExchangeName": "string",
    "CommodityNo": "string",
    "CommodityName": "string",
    "CommodityType": "string",
    "CurrencyNo": "string",
    "CurrencyName": "string",
    "ProductDot": "double",
    "UpperTick": "double",
    "SettlePrice": "double",
    "TradeMonth": "string",
    "DotNum": "int",
    "LowerTick": "int",
    "DotNumCarry": "int",
    "UpperTickCarry": "double",
    "FirstNoticeDay": "string",
    "FreezenPercent": "double",
    "FreezenMoney": "double",
    "FeeMoney": "double",
    "FeePercent": "double",
    "PriceStrike": "double",
    "ProductDotStrike": "double",
    "UpperTickStrike": "double",
    "LastTradeDay": "string",
    "LastUpdateDay": "string",
    "CriticalPrice": "double",
    "CriticalMinChangedPrice": "double",
    "ExchangeSub": "string",
    "OptionType": "string",
    "OptionMonth": "string",
    "OptionStrikePrice": "string",
    "OptionCommodityNo": "string",
    "OptionContractNo": "string",
    "MortgagePercent": "string",
    "UpperTickCode": "string",
    "LotSize": "string",
    "FlatTime": "string",
    "CommodityFNameEN": "string",
    "CanSell": "string",
    "SellRate": "double",
    "SellMax": "double",
    "StrikeRate": "double",
    "StrikePrice": "double",
    "ReceivePrice": "double",
    "ExpireDate": "string",
    "SellRateKeep": "double",
    "StrikeCommodityNo": "string",
    "CallPutFlag": "string",
    "Publisher": "string",
}

CStockQryExchangeField = {
    "ProductGroupID": "string",
    "ErrorDescription": "string",
}

CStockRspExchangeField = {
    "ExchangeNo": "string",
    "ExchangeName": "string",
    "SettleType": "string",
    "NameEN": "string",
}

CStockQryCapitalField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CStockRspCapitalField = {
    "UserId": "string",
    "InMoney": "string",
    "OutMoney": "string",
    "TodayCanUse": "string",
    "TodayAmount": "string",
    "TodayBalance": "string",
    "FreezenMoney": "string",
    "Commission": "string",
    "Margin": "string",
    "OldCanUse": "string",
    "OldAmount": "string",
    "OldBalance": "string",
    "FloatingProfit": "string",
    "CurrencyNo": "string",
    "CurrencyRate": "double",
    "UnexpiredProfit": "double",
    "UnaccountProfit": "double",
    "KeepDeposit": "double",
    "Royalty": "double",
    "Credit": "double",
    "AddCapital": "double",
    "IniEquity": "double",
    "AccountNo": "string",
    "MortgageMoney": "double",
    "MarginLimit": "double",
    "BorrowValue": "double",
    "T1": "double",
    "T2": "double",
    "T3": "double",
    "TN": "double",
    "TradeLimit": "double",
    "CanCashOut": "double",
    "AccruedCrInt": "double",
    "AccruedDrInt": "double",
    "CrossMax": "double",
    "SellFreezenMoney": "double",
    "SellInterest": "double",
    "SellNeedAddMargin": "double",
    "NetProfit": "string",
    "ProfitRate": "string",
    "RiskRate": "string",
    "ErrorDescription": "string",
}

CStockQryPositionField = {
    "ErrorDescription": "string",
}

CStockRspPositionField = {
    "ClientNo": "string",
    "ExchangeNo": "string",
    "CommodityNo": "string",
    "Direct": "string",
    "HoldPrice": "double",
    "CanTradeVol": "int",
    "TodayBuyVol": "int",
    "FrozenVol": "int",
    "TotalBuyMoney": "double",
    "TotalSellMoney": "double",
    "TotalBuyVol": "int",
    "TotalSellVol": "int",
    "OpenDate": "string",
    "FlatProfit": "double",
    "HkexT1": "int",
    "HkexT2": "int",
    "HkexT3": "int",
    "UnsettleVol": "int",
    "SettledVol": "int",
    "HoldVol": "int",
    "TodaySaleVol": "int",
    "SellFrozenMoney": "double",
    "OpenPrice": "double",
}

CStockQryTickField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CStockRspTickField = {
    "UpperTickCode": "string",
    "PriceFrom": "string",
    "UpperTick": "string",
    "ProductDot": "string",
    "DotNum": "string",
    "LowerTick": "string",
}

CStockQryCurrencyField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CStockRspCurrencyField = {
    "CurrencyNo": "string",
    "IsBase": "int",
    "ChangeRate": "double",
    "CurrencyName": "string",
    "CurrencyNameEN": "string",
}

CStockQryVersionField = {
    "UserId": "string",
    "UserPwd": "string",
    "ErrorDescription": "string",
}

CStockRspVersionField = {
    "Version": "string",
    "MustUpdate": "string",
    "MustVersion": "string",
    "VersionContent_CN": "string",
    "VersionContent_US": "string",
}

CStockRtnOrderField = {
    "LocalOrderNo": "string",
    "ExchangeNo": "string",
    "TreatyCode": "string",
    "OrderNo": "string",
    "OrderNumber": "int",
    "FilledNumber": "int",
    "FilledAdvPrice": "double",
    "BuyHoldNumber": "int",
    "BuyHoldOpenPrice": "double",
    "BuyHoldPrice": "double",
    "SaleHoldNumber": "int",
    "SaleHoldOpenPrice": "double",
    "SaleHoldPrice": "double",
    "IsCanceled": "string",
    "FilledTotalFee": "double",
    "Status": "int",
    "AccountNo": "string",
    "HoldType": "string",
    "HoldMarginBuy": "double",
    "HoldMarginSale": "double",
    "CurrPrice": "double",
    "FloatProfit": "double",
}

CStockRtnCapitalField = {
    "ClientNo": "string",
    "AccountNo": "string",
    "CurrencyNo": "string",
    "Available": "double",
    "YAvailable": "double",
    "CanCashOut": "double",
    "Money": "double",
    "ExpiredProfit": "double",
    "FrozenDeposit": "double",
    "Fee": "double",
    "Deposit": "double",
    "KeepDeposit": "double",
    "Status": "int",
    "InMoney": "double",
    "OutMoney": "double",
    "UnexpiredProfit": "double",
    "TodayTotal": "double",
    "UnaccountProfit": "double",
    "Royalty": "double",
    "ExchangeNo": "string",
    "TreatyCode": "string",
    "OrderNo": "string",
    "OrderNumber": "int",
    "FilledNumber": "int",
    "FilledAdvPrice": "double",
    "BuyHoldNumber": "int",
    "BuyHoldOpenPrice": "double",
    "BuyHoldPrice": "double",
    "SaleHoldNumber": "int",
    "SaleHoldOpenPrice": "double",
    "SaleHoldPrice": "double",
    "IsCanceled": "string",
    "FilledTotalFee": "double",
    "Credit": "double",
    "MarginLimit": "double",
    "BorrowValue": "double",
    "MortgageMoney": "double",
    "T1": "double",
    "T2": "double",
    "T3": "double",
    "TN": "double",
    "TradeLimit": "double",
    "FCrossMax": "double",
    "SellFreezenMoney": "double",
    "SellInterest": "double",
    "SellNeedAddMargin": "double",
}

CStockRtnPositionField = CStockRspPositionField

CStockRtnTradeField = CStockRspTradeField

CStockReqGetQuestionField = {
    "Unused": "int",
    "ErrorDescription": "string",
}

CStockRspQuestionField = {
    "QuestionType": "string",
    "QuestionId": "string",
    "QuestionCN": "string",
    "QuestionEN": "string",
}

CStockReqSafeVerifyField = {
    "UserId": "string",
    "UserPwd": "string",
    "Type": "string",
    "Question": "string",
    "Answer": "string",
    "MobileNumber": "string",
    "VerifyCode": "string",
    "SaveMac": "string",
    "MacAddress": "string",
    "ErrorDescription": "string",
}

CStockReqSetVerifyQAField = {
    "UserId": "string",
    "UserPwd": "string",
    "Type": "string",
    "Question": "string",
    "Answer": "string",
    "MobileNumber": "string",
    "VerifyCode": "string",
    "SaveMac": "string",
    "ErrorDescription": "string",
}

CStockReqVerifyCodeField = {
    "UserId": "string",
    "UserPwd": "string",
    "Type": "string",
    "Question": "string",
    "Answer": "string",
    "MobileNumber": "string",
    "VerifyCode": "string",
    "ErrorDescription": "string",
}

