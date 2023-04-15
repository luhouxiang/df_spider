-- 板块资金流向表
CREATE TABLE IF NOT EXISTS `tbl_bk_fin_flow` (
    `TradingDay` int(11) DEFAULT 0 COMMENT '交易日',
    `BkName` varchar(20) DEFAULT '' COMMENT '操作类型，open,reopen,close,change',
    `SerialNo` int(11) DEFAULT 0 COMMENT '序号',
    `TodayZdf` decimal(18,2) DEFAULT 0 COMMENT '今日涨跌幅，数值扩大100倍',
    `TodayMainNet` decimal(18,2) DEFAULT 0 COMMENT '今日主力净流入净额',
    `TodayMainRate` decimal(18,2) DEFAULT 0 COMMENT '今日主力净流入占比，数值扩大100倍',
    `TodayLargeNet` decimal(18,2) DEFAULT 0 COMMENT '今日超大单净流入净额',
    `TodayLargeRate` decimal(18,2) DEFAULT 0 COMMENT '今日超大单净流入占比，数值扩大100倍',
    `TodayBigNet` decimal(18,2) DEFAULT 0 COMMENT '今日大单净流入净额',
    `TodayBigRate` decimal(18,2) DEFAULT 0 COMMENT '今日大单净流入占比，数值扩大100倍',
    `TodayMiddleNet` decimal(18,2) DEFAULT 0 COMMENT '今日中单净流入净额',
    `TodayMiddleRate` decimal(18,2) DEFAULT 0 COMMENT '今日中单净流入占比，数值扩大100倍',
    `TodaySmallNet` decimal(18,2) DEFAULT 0 COMMENT '今日小单净流入净额',
    `TodaySmallRate` decimal(18,2) DEFAULT 0 COMMENT '今日小单净流入占比，数值扩大100倍',
    `DelegateName` varchar(20) DEFAULT '' COMMENT '今日主力净流入最大股',
    `KlineTime` datetime NOT NULL COMMENT 'K线时间，即对应上证指数的K线时间',
    `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`TradingDay`, `BkName`),
    INDEX  index_tbl_tbl_bk_fin_flow_01  (TradingDay)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 东方财富交易日
CREATE TABLE IF NOT EXISTS `tbl_trading_day` (
    `TradingDay` int(11) DEFAULT 0 COMMENT '交易日',
    `KlineTime` datetime NOT NULL COMMENT 'K线时间，即对应上证指数的K线时间',
    `ServerTime` datetime NOT NULL COMMENT '服务器时间',
    `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`TradingDay`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

