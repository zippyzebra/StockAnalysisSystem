import logging
import collections
from os import sys, path
from datetime import datetime
root_path = path.dirname(path.dirname(path.abspath(__file__)))

try:
    from Utiltity.common import *
    from Database.DatabaseEntry import DatabaseEntry
    from Utiltity.plugin_manager import PluginManager
    from DataHub.DataUtility import DataUtility
    from DataHub.UniversalDataCenter import ParameterChecker
    from DataHub.UniversalDataCenter import UniversalDataTable
    from DataHub.UniversalDataCenter import UniversalDataCenter
except Exception as e:
    sys.path.append(root_path)

    from Utiltity.common import *
    from Database.DatabaseEntry import DatabaseEntry
    from Utiltity.plugin_manager import PluginManager
    from DataHub.DataUtility import DataUtility
    from DataHub.UniversalDataCenter import ParameterChecker
    from DataHub.UniversalDataCenter import UniversalDataTable
    from DataHub.UniversalDataCenter import UniversalDataCenter
finally:
    logger = logging.getLogger('')


NOT_SPEC = {
}

A_SHARE_MARKET = ['SSE', 'SZSE']
ALL_SHARE_MARKET = ['SSE', 'SZSE', 'CSI', 'CICC', 'SW', 'MSCI', 'OTH']

# Too much indexes (more than 9000)
# Hard coded. Select form TestData/Market_IndexInfo.csv
# TODO: Configurable

DEPENDS_INDEX = collections.OrderedDict([
    ('000001.SSE', '上证综指'),
    ('000002.SSE', '上证A指'),
    ('000003.SSE', '上证B指'),
    ('000016.SSE', '上证50'),
    ('399001.SESZ', '深证成指'),
    ('399005.SESZ', '中小板指'),
    ('399006.SESZ', '创业板指'),
])


# Principle: Only declare the minimal common field
# 原则：只限制通用字段且限制的字段尽可能少

# ---------------------- Market.NamingHistory ---------------------


QUERY_FIELDS_NAMING_HISTORY = {
    'stock_identity': ([str], [],                   False,  ''),
    'naming_date':    ([tuple, datetime, None], [], False,  ''),
}

RESULT_FIELDS_NAMING_HISTORY = {
    'stock_identity': (['str'], [],                 True,  ''),
    'name':           (['str'], [],                 True,  ''),
    'naming_date':    (['datetime'], [],            True,  ''),
}


# --------------------- Market.IndexInfo ---------------------

QUERY_FIELDS_INDEX_INFO = {
    'index_identity': ([str], [],                   False,  ''),
    'exchange':       ([str], ALL_SHARE_MARKET,     False,  ''),
}

RESULT_FIELDS_INDEX_INFO = {
    'index_identity': (['str'], [],                 True,  ''),
    'code':           (['str'], [],                 True,  ''),
    'name':           (['str'], [],                 True,  ''),
    'fullname':       (['str'], [],                 True,  ''),
    'exchange':       (['str'], ALL_SHARE_MARKET,   True,  ''),
    'publisher':      (['str'], [],                 True,  ''),
    'listing_date':   (['datetime'], [],            True,  ''),
}


# --------------------- Market.TradeCalender ---------------------

QUERY_FIELDS_TRADE_CALENDER = {
    'exchange':     ([str], ['SSE', 'SZSE', 'A-SHARE'], True,  ''),
    'trade_date':   ([tuple], [],                       False,  ''),
}

RESULT_FIELDS_TRADE_CALENDER = {
    'exchange':     (['str'], ['SSE', 'SZSE'],  True,  ''),
    'trade_date':   (['datetime'], [],          True,  ''),
    'status':       (['int'], [],               True,  ''),
}


# --------------------- Market.SecuritiesInfo ---------------------

QUERY_FIELDS_SECURITIES_INFO = {
    'stock_identity': ([str], [],                   False,  ''),
}

RESULT_FIELDS_SECURITIES_INFO = {
    'stock_identity': (['str'], [],                 True,  ''),
    'code':           (['str'], [],                 True,  ''),
    'name':           (['str'], [],                 True,  ''),
    'exchange':       (['str'], A_SHARE_MARKET,     True,  ''),
    'listing_date':   (['datetime'], [],            True,  ''),
}


# --------------------- Market.SecuritiesTags ---------------------

QUERY_FIELDS_SECURITIES_TAGS = {
    'stock_identity': ([str], [],           False, ''),
}

RESULT_FIELDS_SECURITIES_TAGS = {
    'stock_identity': (['str'], [],         True, ''),
}

# ---------------------- FinanceData.Audit ----------------------

QUERY_FIELDS_FINANCE_AUDIT = {
    'stock_identity': ([str], [],                           False, ''),
    'period':         ([tuple,  None], [],                  False, ''),
}

RESULT_FIELDS_FINANCE_AUDIT = {
    'stock_identity': (['str'], [],         True, ''),
    'period':         (['datetime'], [],    True, ''),                  # The last day of report period
    'conclusion':     (['str'], [],         True, '审计结果'),
    'agency': (['str'], [],                 True, '会计事务所'),
    'sign': (['str'], [],                   True, '签字会计师'),
}

# ------------------------ FinanceData.* ------------------------

QUERY_FIELDS_FINANCE_DATA = {
    'stock_identity': ([str], [],                           False, ''),
    'period':         ([tuple,  None], [],                  False, ''),
}

RESULT_FIELDS_FINANCE_DATA = {
    'stock_identity': (['str'], [],         True, ''),
    'period':         (['datetime'], [],    True, ''),                # The last day of report period
}

RESULT_FIELDS_MAIN_BUSINESS = {
    'stock_identity': (['str'], [],         True, ''),
    'period':         (['datetime'], [],    True, ''),                # The last day of report period
    'business':       (['dict'], [],        True, ''),
}

# ------------------------ Stockholder.PledgeStatus ------------------------

QUERY_FIELDS_PLEDGE_STATUS = {
    'stock_identity': ([str], [],                           False, ''),
    'due_date':       ([tuple,  None], [],                  False, ''),
}

RESULT_FIELDS_PLEDGE_STATUS = {
    'stock_identity': (['str'], [],         True, ''),
    'due_date':       (['datetime'], [],    True, ''),
    'pledge_count':   (['int'], [],         True, ''),
    'pledge_ratio':   (['float'], [],       True, ''),
}

# ------------------------ Stockholder.PledgeHistory ------------------------

QUERY_FIELDS_PLEDGE_HISTORY = {
    'stock_identity': ([str], [],                           False, ''),
    'due_date':       ([tuple,  None], [],                  False, ''),
}

RESULT_FIELDS_PLEDGE_HISTORY = {
    # TODO: TBD
    'stock_identity': (['str'], [],         True, ''),
    'due_date':       (['datetime'], [],    True, ''),
}

# ------------------------ Stockholder.Statistics ------------------------

QUERY_FIELDS_STOCKHOLDER_STATISTICS = {
    'stock_identity': ([str], [],                           False, ''),
    'period':         ([tuple,  None], [],                  False, ''),
}

RESULT_FIELDS_STOCKHOLDER_STATISTICS = {
    'stock_identity':                   (['str'], [],       True, ''),
    'period':                           (['datetime'], [],  True, ''),
    'stock_holder_count':               (['int'], [],       False, ''),

    # [{name: '', amount: '', ratio: '', ...} x 10]
    # nt = non_tradable
    'stockholder_top10':                (['list'], [],      False, ''),
    'stockholder_top10_nt':             (['list'], [],      False, ''),
}

# ------------------------ TradeData.Daily ------------------------

QUERY_FIELDS_TRADE_DAILY = {
    'stock_identity': ([str], [],           True,  ''),
    'trade_date':     ([tuple, None], [],   False, ''),
}

RESULT_FIELD_TRADE_DAILY = {
    'trade_date':     (['datetime'], [],    True, ''),
}


# --------------------------------------- UniversalDataTableSeparate ---------------------------------------

class IdentityTableExtender(UniversalDataTable.Extender):
    def __init__(self):
        super(IdentityTableExtender, self).__init__()

    def parts(self, uri: str, identity: str or [str], time_serial: tuple, extra: dict, fields: list) -> \
            [(str, str or [str], tuple, dict, list)]:
        if not isinstance(identity, (list, tuple)):
            identity = [identity]
        return [(uri, _id, time_serial, extra, fields) for _id in identity]

    def table_name(self, uri: str, identity: str, time_serial: tuple, extra: dict, fields: list) -> str:
        name = (uri + '_' + identity) if str_available(identity) else uri
        return name.replace('.', '_')


# ---------------------------------------- Declare ----------------------------------------

DFTDB = 'StockAnalysisSystem'
DFTPRX = ''

DATA_FORMAT_URI = 0
DATA_FORMAT_DATABASE = 1
DATA_FORMAT_TABLE_PREFIX = 2
DATA_FORMAT_IDENTITY_FIELD = 3
DATA_FORMAT_DATETIME_FIELD = 4
DATA_FORMAT_QUERY_FIELD_INFO = 5
DATA_FORMAT_RESULT_FIELD_INFO = 6

DATA_FORMAT_DECLARE = [
    ('Market.SecuritiesInfo', DFTDB, DFTPRX, 'stock_identity', None,          QUERY_FIELDS_SECURITIES_INFO, RESULT_FIELDS_SECURITIES_INFO),
    ('Market.IndexInfo',      DFTDB, DFTPRX, 'index_identity', None,          QUERY_FIELDS_INDEX_INFO, RESULT_FIELDS_INDEX_INFO),

    ('Market.SecuritiesTags', DFTDB, DFTPRX, 'stock_identity', None,          QUERY_FIELDS_SECURITIES_TAGS, RESULT_FIELDS_SECURITIES_TAGS),

    ('Market.TradeCalender',  DFTDB, DFTPRX, 'exchange', 'trade_date',        QUERY_FIELDS_TRADE_CALENDER,  RESULT_FIELDS_TRADE_CALENDER),
    ('Market.NamingHistory',  DFTDB, DFTPRX, 'stock_identity', 'naming_date', QUERY_FIELDS_NAMING_HISTORY, RESULT_FIELDS_NAMING_HISTORY),

    ('Finance.Audit',               DFTDB, DFTPRX, 'stock_identity', 'period', QUERY_FIELDS_FINANCE_AUDIT, RESULT_FIELDS_FINANCE_AUDIT),
    ('Finance.BalanceSheet',        DFTDB, DFTPRX, 'stock_identity', 'period', QUERY_FIELDS_FINANCE_DATA, RESULT_FIELDS_FINANCE_DATA),
    ('Finance.IncomeStatement',     DFTDB, DFTPRX, 'stock_identity', 'period', QUERY_FIELDS_FINANCE_DATA, RESULT_FIELDS_FINANCE_DATA),
    ('Finance.CashFlowStatement',   DFTDB, DFTPRX, 'stock_identity', 'period', QUERY_FIELDS_FINANCE_DATA, RESULT_FIELDS_FINANCE_DATA),
    ('Finance.BusinessComposition', DFTDB, DFTPRX, 'stock_identity', 'period', QUERY_FIELDS_FINANCE_DATA, RESULT_FIELDS_MAIN_BUSINESS),

    ('Stockholder.PledgeStatus',  DFTDB, DFTPRX, 'stock_identity', 'due_date', QUERY_FIELDS_PLEDGE_STATUS, RESULT_FIELDS_PLEDGE_STATUS),
    ('Stockholder.PledgeHistory', DFTDB, DFTPRX, 'stock_identity', 'due_date', QUERY_FIELDS_PLEDGE_HISTORY, RESULT_FIELDS_PLEDGE_HISTORY),
    ('Stockholder.Statistics',    DFTDB, DFTPRX, 'stock_identity', 'period',   QUERY_FIELDS_STOCKHOLDER_STATISTICS, RESULT_FIELDS_STOCKHOLDER_STATISTICS),

    ('TradeData.Stock.Daily',     'StockDaily', DFTPRX, 'stock_identity', 'trade_date', QUERY_FIELDS_TRADE_DAILY, RESULT_FIELD_TRADE_DAILY),
    ('TradeData.Index.Daily',     'StockDaily', DFTPRX, 'stock_identity', 'trade_date', QUERY_FIELDS_TRADE_DAILY, RESULT_FIELD_TRADE_DAILY),
]

SPECIAL_EXTENDER_TABLE = {
    'TradeData.Stock.Daily': IdentityTableExtender(),
    'TradeData.Index.Daily': IdentityTableExtender(),
}


class DataHubEntry:
    def __init__(self, database_entry: DatabaseEntry, collector_plugin: PluginManager):
        self.__database_entry = database_entry
        self.__collector_plugin = collector_plugin
        self.__data_center = UniversalDataCenter(database_entry, collector_plugin)
        self.__data_utility = DataUtility(self.__data_center)
        self.build_data_table()

    def get_data_center(self) -> UniversalDataCenter:
        return self.__data_center

    def get_data_utility(self) -> DataUtility:
        return self.__data_utility

    # ------------------------------------------------------------------------------------------------------------------

    def build_data_table(self):
        for data_format in DATA_FORMAT_DECLARE:
            if not DataHubEntry.check_data_format(data_format):
                print('Error data declare format: ' + data_format[DATA_FORMAT_URI])
                continue
            self.get_data_center().register_data_table(
                UniversalDataTable(data_format[DATA_FORMAT_URI], self.__database_entry,
                                   data_format[DATA_FORMAT_DATABASE], data_format[DATA_FORMAT_TABLE_PREFIX],
                                   data_format[DATA_FORMAT_IDENTITY_FIELD], data_format[DATA_FORMAT_DATETIME_FIELD],
                                   SPECIAL_EXTENDER_TABLE.get(data_format[DATA_FORMAT_URI], None)),
                ParameterChecker(data_format[DATA_FORMAT_RESULT_FIELD_INFO],
                                 data_format[DATA_FORMAT_QUERY_FIELD_INFO])
            )

    @staticmethod
    def check_data_format(data_format: tuple) -> bool:
        if len(data_format) != 7:
            print('Error: The size of data format declare should be 7.')
            return False

        if not isinstance(data_format[DATA_FORMAT_URI], str):
            print('Error: The uri (index: %s) should be str.' % DATA_FORMAT_URI)
            return False
        if not isinstance(data_format[DATA_FORMAT_DATABASE], str):
            print('Error: The database name (index: %s) should be str.' % DATA_FORMAT_DATABASE)
            return False
        if not isinstance(data_format[DATA_FORMAT_TABLE_PREFIX], str):
            print('Error: The table prefix (index: %s) should be str.' % DATA_FORMAT_TABLE_PREFIX)
            return False

        if data_format[DATA_FORMAT_IDENTITY_FIELD] is not None and \
                not isinstance(data_format[DATA_FORMAT_IDENTITY_FIELD], str):
            print('Error: The identity field (index: %s) should be None or str.' % DATA_FORMAT_IDENTITY_FIELD)
            return False
        if data_format[DATA_FORMAT_DATETIME_FIELD] is not None and \
                not isinstance(data_format[DATA_FORMAT_DATETIME_FIELD], str):
            print('Error: The datetime field (index: %s) should be None or str.' % DATA_FORMAT_DATETIME_FIELD)
            return False

        if not isinstance(data_format[DATA_FORMAT_QUERY_FIELD_INFO], dict):
            print('Error: The query format (index: %s) should be None or str.' % DATA_FORMAT_QUERY_FIELD_INFO)
            return False
        if not isinstance(data_format[DATA_FORMAT_RESULT_FIELD_INFO], dict):
            print('Error: The result format (index: %s) should be None or str.' % DATA_FORMAT_RESULT_FIELD_INFO)
            return False

        if not DataHubEntry.check_query_result_declare(data_format[DATA_FORMAT_QUERY_FIELD_INFO]):
            print('Query format declare error.')
            return False
        if not DataHubEntry.check_query_result_declare(data_format[DATA_FORMAT_RESULT_FIELD_INFO]):
            print('Result format declare error.')
            return False
        return True

    @staticmethod
    def check_query_result_declare(dec: dict) -> bool:
        for key in dec:
            val = dec[key]
            if len(val) != 4 or \
                    not isinstance(val[0], list) or \
                    not isinstance(val[1], list) or \
                    not isinstance(val[2], bool) or \
                    not isinstance(val[3], str):
                print('Result format declare error.')
                return False
        return True





























        # self.__finance_data = FinanceData(collector_plugin, database_entry.get_update_table())
        # self.__trade_calendar = TradeCalendar(collector_plugin, database_entry.get_update_table())
        # self.__securities_info = SecuritiesInfo(collector_plugin, database_entry.get_update_table())
        #
        # database_entry.get_alias_table().register_participant(self.__finance_data)

    # def get_finance_data(self):
    #     return self.__finance_data
    #
    # def get_trade_calendar(self):
    #     return self.__trade_calendar
    #
    # def get_securities_info(self):
    #     return self.__securities_info
