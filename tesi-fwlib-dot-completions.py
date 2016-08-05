import sublime, sublime_plugin

completions = []
dotcompletions = {}

dotcompletions['application'] = [
  ('lib_array','lib_array'),
  ('lib_dt','lib_dt'),
  ('lib_misc','lib_misc'),
  ('lib_org','lib_org'),
  ('lib_query','lib_query'),
  ('lib_search_fso','lib_search_fso'),
  ('lib_show','lib_show'),
  ('lib_str','lib_str'),
  ('lib_struct','lib_struct'),
  ('lib_ui','lib_ui'),
  ('lib_url','lib_url')
]

dotcompletions['lib_array'] = [
  ('lib_array_concat','lib_array_concat(${1:${2:array_1 ARRAY}, ${3:array_2 ARRAY}})'),
  ('ArrayReverse','ArrayReverse(${1:${2:[inArray] }})'),
  ('arrayOfStructuresDeleteDuplicates','arrayOfStructuresDeleteDuplicates(${1:${2:inputArray ARRAY}})'),
  ('ListDeleteDuplicatesNoCase','ListDeleteDuplicatesNoCase(${1:${2:[list] STRING}, ${3:[delimiter] STRING}})'),
  ('listToArray_multichar_sep','listToArray_multichar_sep(${1:${2:[list] }, ${3:[sep] }})'),
  ('ListDeleteDuplicates','ListDeleteDuplicates(${1:${2:[list] STRING}, ${3:[delimiter] STRING}})'),
  ('indexExists','indexExists(${1:${2:array ARRAY}, ${3:index NUMERIC}})'),
  ('ArrayConcat','ArrayConcat(${1:${2:[a1] }, ${3:[a2] }})'),
  ('arraySlice','arraySlice(${1:${2:arr ARRAY}, ${3:[begin] NUMERIC}, ${4:[length] NUMERIC}})'),
  ('ArrayFind','ArrayFind(${1:${2:array ARRAY}, ${3:element STRING}, ${4:[searchInStructValues] BOOLEAN}, ${5:[structKey] STRING}, ${6:[delimiter] STRING}})'),
  ('arrayOfStructuresHasDupFields','arrayOfStructuresHasDupFields(${1:${2:inputArray ARRAY}, ${3:field STRING}})'),
  ('init_matrix','init_matrix(${1:${2:dim_y NUMERIC}, ${3:dim_x NUMERIC}, ${4:fill_value STRING}, ${5:[debug] BOOLEAN}})'),
  ('arrayOfStructuresToQuery','arrayOfStructuresToQuery(${1:${2:theArray ARRAY}, ${3:[columns] STRING}, ${4:[setColumnsType] BOOLEAN}, ${5:[columnsType] STRING}, ${6:[orderBy] STRING}})'),
  ('arrayOfStructsSort','arrayOfStructsSort(${1:${2:[aOfS] }, ${3:[key] }})'),
  ('normalize','normalize(${1:${2:[array] ARRAY}, ${3:[deleteUndefined] BOOLEAN}, ${4:[substitutionValue] ANY}})'),
  ('queryToArrayOfStructures','queryToArrayOfStructures(${1:${2:theQuery QUERY}, ${3:[colsToExclude] STRING}})'),
  ('stringToArray','stringToArray(${1:${2:[string] }, ${3:[count] }})')
]

dotcompletions['lib_dt'] = [
  ('dayStart','dayStart(${1:${2:date DATE}})'),
  ('getComboOre','getComboOre(${1:${2:[risoluzione] NUMERIC}})'),
  ('seconds2time','seconds2time(${1:${2:seconds NUMERIC}, ${3:[keys2view] STRING}})'),
  ('lib_validate_dates','lib_validate_dates(${1:${2:[start_date] }, ${3:[end_date] }, ${4:[date_format] }})'),
  ('nvldate','nvldate(${1:${2:data }})'),
  ('joinTimestamps','joinTimestamps(${1:${2:date }, ${3:[time] }})'),
  ('getWeekDates','getWeekDates(${1:${2:[date] DATE}, ${3:[firstDayOfWeek] NUMERIC}})'),
  ('getOreLavorativePeriodo','getOreLavorativePeriodo(${1:${2:idSocieta STRING}, ${3:idAnagrafica STRING}, ${4:dataDa DATE}, ${5:dataA DATE}, ${6:globals STRUCT}, ${7:[dbprop] STRUCT}, ${8:[idcalendar] STRING}})'),
  ('overlapping_period','overlapping_period(${1:${2:p1_start DATE}, ${3:p1_end DATE}, ${4:p2_start DATE}, ${5:p2_end DATE}, ${6:[datepart] STRING}})'),
  ('getWeekStartDate','getWeekStartDate(${1:${2:weekNum NUMERIC}, ${3:weekYear NUMERIC}})'),
  ('time2seconds','time2seconds(${1:${2:[time_struct] }})'),
  ('getWeekNumber','getWeekNumber(${1:${2:date DATE}})'),
  ('yyyymmdd2date','yyyymmdd2date(${1:${2:yyyymmdd STRING}})'),
  ('drawDatePicker','drawDatePicker(${1:${2:[input_name] STRING}, ${3:[input_id] STRING}, ${4:[default_value] STRING}, ${5:[form_index] STRING}, ${6:[with_calendar] STRING}, ${7:[calendar_img] STRING}, ${8:[disabled] BOOLEAN}, ${9:[disabled_value] STRING}, ${10:[start_date] STRING}, ${11:[onchange] STRING}, ${12:[class] STRING}, ${13:[class_calendar] STRING}, ${14:[input_name_hidden] STRING}, ${15:[readonly] BOOLEAN}, ${16:[html_attr] STRING}, ${17:[onblur] STRING}, ${18:[shiftDate_enable] BOOLEAN}, ${19:[onshiftDate] STRING}, ${20:[onkeypress] STRING}})'),
  ('getTimeStamp','getTimeStamp()'),
  ('getNumericTimestamp','getNumericTimestamp(${1:${2:[dateTimeSep] STRING}, ${3:[includeMilliseconds] BOOLEAN}, ${4:[today] DATE}})'),
  ('convertISOToDatetime','convertISOToDatetime(${1:${2:Data STRING}})'),
  ('seconds2HHMMSS','seconds2HHMMSS(${1:${2:[seconds] }})'),
  ('getDatePickerCfg','getDatePickerCfg()'),
  ('drawTimePicker','drawTimePicker(${1:${2:[input_name] STRING}, ${3:[input_id] STRING}, ${4:[default_value] STRING}, ${5:[disabled] BOOLEAN}, ${6:[disabled_value] STRING}, ${7:[with_seconds] BOOLEAN}, ${8:[sep] STRING}, ${9:[onchange] STRING}, ${10:[attr_html] STRING}, ${11:[class] STRING}, ${12:[default_ret] STRING}, ${13:[debug] BOOLEAN}})'),
  ('getOreLavorative','getOreLavorative(${1:${2:idSocieta STRING}, ${3:idAnagrafica STRING}, ${4:data DATE}, ${5:globals STRUCT}, ${6:[dbprop] STRUCT}})'),
  ('getYearDates','getYearDates(${1:${2:[date] DATE}})'),
  ('timestamp','timestamp()'),
  ('businessDaysBetween','businessDaysBetween(${1:${2:[date1] }, ${3:[date2] }})'),
  ('lib_create_odate_time','lib_create_odate_time(${1:${2:[dd_mm_yyyy] STRING}, ${3:[hh_mm] STRING}, ${4:[return_date] BOOLEAN}, ${5:[return_midnight] BOOLEAN}})'),
  ('LastDayOfMonth','LastDayOfMonth(${1:${2:[strMonth] }})'),
  ('getHalfYearDates','getHalfYearDates(${1:${2:[date] DATE}})'),
  ('dayEnd','dayEnd(${1:${2:date DATE}})'),
  ('Int_Week','Int_Week(${1:${2:[arg_data_da] }})'),
  ('getMonthDates','getMonthDates(${1:${2:[date] DATE}})'),
  ('sortDateList','sortDateList(${1:${2:dates STRING}, ${3:[sort_order] STRING}, ${4:[mask] STRING}})'),
  ('lib_validate_times','lib_validate_times(${1:${2:[start_time] }, ${3:[end_time] }, ${4:[time_format] }})'),
  ('minDate','minDate(${1:${2:date1 DATE}, ${3:date2 DATE}})'),
  ('lib_create_odate','lib_create_odate(${1:${2:dd_mm_yyyy STRING}, ${3:[return_date] BOOLEAN}})'),
  ('getQuarterDates','getQuarterDates(${1:${2:[date] DATE}})'),
  ('getPrimoGgFeriale','getPrimoGgFeriale(${1:${2:idSocieta STRING}, ${3:idTipoCalendario STRING}, ${4:dataDaValutare DATE}, ${5:[dataLimite] DATE}, ${6:[giorniFestivi] STRING}, ${7:dbprop STRUCT}})'),
  ('maxDate','maxDate(${1:${2:date1 DATE}, ${3:date2 DATE}})'),
  ('addBusinessDays','addBusinessDays(${1:${2:[date] }, ${3:[days] }})'),
  ('datediffwithCalendar','datediffwithCalendar(${1:${2:[datePart] STRING}, ${3:date1 DATE}, ${4:date2 DATE}, ${5:[countSaturday] BOOLEAN}, ${6:[countSunday] BOOLEAN}, ${7:[idSocieta] STRING}, ${8:[idCalendar] STRING}, ${9:dbprop STRUCT}})'),
  ('dateAddWithCalendar','dateAddWithCalendar(${1:${2:datepart STRING}, ${3:number NUMERIC}, ${4:date DATE}, ${5:idsocieta STRING}, ${6:idcalendar STRING}})')
]

dotcompletions['lib_misc'] = [
  ('min_number','min_number()'),
  ('init_numeri','init_numeri()'),
  ('scrambleVowels','scrambleVowels(${1:${2:str STRING}})'),
  ('verifyOrgRoleInSession','verifyOrgRoleInSession(${1:${2:session_info STRUCT}, ${3:idorg STRING}, ${4:idruolo STRING}})'),
  ('setRich_UrlGoback','setRich_UrlGoback(${1:${2:[args_struct] }, ${3:[args_goback_key] }, ${4:[session_urlgoback_key] }})'),
  ('maskColumns','maskColumns(${1:${2:[tables] STRUCT}, ${3:dbprop STRUCT}})'),
  ('initComponents','initComponents(${1:${2:[components] STRUCT}, ${3:[isSingleton] BOOLEAN}, ${4:[singletonScope] STRING}})'),
  ('lib_get_process_vars','lib_get_process_vars(${1:${2:const STRUCT}, ${3:the_session STRUCT}})'),
  ('completeSQLErrorDetails','completeSQLErrorDetails(${1:${2:[errorDetails] ANY}, ${3:[sql] STRING}, ${4:[where] STRING}})'),
  ('logArguments','logArguments(${1:${2:[struct2log] STRUCT}, ${3:[logfile] STRING}})'),
  ('queryAddColumnWithValue','queryAddColumnWithValue(${1:${2:query QUERY}, ${3:column_name STRING}, ${4:[value] STRING}, ${5:[datatype] STRING}})'),
  ('GetTemplateName','GetTemplateName()'),
  ('map_pages','map_pages(${1:${2:[struct_to_fill] STRUCT}, ${3:struct_name STRING}, ${4:[set_structs] ARRAY}, ${5:[set_common_prefix] ARRAY}, ${6:[set_default_rule] ARRAY}, ${7:[default_rule] STRING}, ${8:[list_subkey_len] STRING}, ${9:my_session STRUCT}, ${10:[debug] BOOLEAN}})'),
  ('getMailForSysNotify','getMailForSysNotify(${1:${2:[idorg] STRING}, ${3:[idruolo] STRING}, ${4:sessionInfo STRUCT}})'),
  ('setResourcesPath','setResourcesPath(${1:${2:resources STRUCT}, ${3:[sessionInfo] STRUCT}, ${4:[debug] BOOLEAN}})'),
  ('getGlobals','getGlobals()'),
  ('lib_get_array_ruoli','lib_get_array_ruoli(${1:${2:[getRuoliLogici] BOOLEAN}})'),
  ('calcolaArrotondamento','calcolaArrotondamento(${1:${2:importo NUMERIC}, ${3:arrotondamento NUMERIC}, ${4:tipoArrotondamento STRING}, ${5:dbprop STRUCT}, ${6:[debug] BOOLEAN}})'),
  ('max_number','max_number()'),
  ('toWDDX','toWDDX(${1:${2:action STRING}, ${3:input ANY}})'),
  ('lib_set_range','lib_set_range(${1:${2:[first] }, ${3:[last] }, ${4:[delta] }})'),
  ('trackDownload','trackDownload(${1:${2:[idsocieta] STRING}, ${3:[idanag] STRING}, ${4:[pathname] STRING}, ${5:[hash] STRING}, ${6:[iddoc] STRING}, ${7:[success] STRING}, ${8:[note] STRING}, ${9:[origine] STRING}, ${10:dbprop STRUCT}, ${11:[downloadToken] STRING}})'),
  ('secureSerialize','secureSerialize(${1:${2:obj ANY}, ${3:[secretKey] STRING}, ${4:[algorithm] STRING}, ${5:[encoding] STRING}})'),
  ('getBrowserLanguage','getBrowserLanguage(${1:${2:[defaultLanguage] STRING}})'),
  ('getFileCrc32','getFileCrc32(${1:${2:filePath STRING}})'),
  ('getCtPath','getCtPath(${1:${2:[cfAdminPassword] STRING}})'),
  ('init_my_struct','init_my_struct(${1:${2:[my_struct] }, ${3:[tipoStruct] }})'),
  ('getEnvironmentLanguage','getEnvironmentLanguage()'),
  ('init_lettere','init_lettere()'),
  ('dot_escape','dot_escape(${1:${2:str2escape STRING}})'),
  ('createMixin','createMixin(${1:${2:target ANY}, ${3:source ANY}, ${4:[overwrite] BOOLEAN}, ${5:[filter] STRING}, ${6:[mappings] STRING}})'),
  ('getResourcesStruct','getResourcesStruct(${1:${2:source STRUCT}})'),
  ('deserializeForm','deserializeForm(${1:${2:serializedForm STRING}, ${3:[dateFields] STRING}})'),
  ('parseSystemVariablesString','parseSystemVariablesString(${1:${2:[variableString] STRING}, ${3:sessionData STRUCT}, ${4:[startVariableDelimiter] STRING}, ${5:[endVariableDelimiter] STRING}, ${6:[systemVariables] STRUCT}, ${7:[quoteStringVariables] BOOLEAN}, ${8:dbprop STRUCT}})'),
  ('resetCFHtmlHead','resetCFHtmlHead()'),
  ('getWatermarkBean','getWatermarkBean(${1:${2:[beanIdentifier] STRING}})'),
  ('do_sleep','do_sleep(${1:${2:[ms] }})'),
  ('generatePassword','generatePassword(${1:${2:[seed] NUMERIC}, ${3:[length] NUMERIC}, ${4:[min_length] }})'),
  ('lib_min_pos_number','lib_min_pos_number()'),
  ('isActiveModule','isActiveModule(${1:${2:[module] }})'),
  ('converti','converti(${1:${2:num STRING}})'),
  ('secureDeSerialize','secureDeSerialize(${1:${2:str STRING}, ${3:secretKey STRING}, ${4:[algorithm] STRING}, ${5:[encoding] STRING}})'),
  ('browserDetect','browserDetect(${1:${2:[UserAgent] STRING}})'),
  ('cerca','cerca(${1:${2:num NUMERIC}, ${3:array ARRAY}})'),
  ('getPackageNameFromPath','getPackageNameFromPath(${1:${2:[path] STRING}, ${3:[pathSep] STRING}})'),
  ('download_file','download_file(${1:${2:down_page_url STRING}, ${3:file_path STRING}, ${4:[file_name_onsave] STRING}, ${5:[deleteFileAfterDownload] BOOLEAN}, ${6:[applyWatermark] BOOLEAN}, ${7:[applyWatermarkIntoZip] BOOLEAN}, ${8:[watermarkManager] ANY}, ${9:[watermarkBean] ANY}, ${10:[TypeAttach] STRING}, ${11:[MimeType] STRING}, ${12:[iddoc] STRING}, ${13:[windowOptions] STRING}, ${14:[target] STRING}, ${15:[downloadToken] STRING}})'),
  ('dividi','dividi(${1:${2:n0 NUMERIC}})'),
  ('initResourcesStruct','initResourcesStruct()')
]

dotcompletions['lib_org'] = [
  ('resp_exists','resp_exists(${1:${2:[arr_resp] }})'),
  ('explodeorg2query','explodeorg2query(${1:${2:idsocieta STRING}, ${3:arr_eo ARRAY}, ${4:dbprop STRUCT}})'),
  ('lib_get_resp_assenze','lib_get_resp_assenze(${1:${2:[struct_var] }})')
]

dotcompletions['lib_query'] = [
  ('getBounds','getBounds(${1:${2:totalRows NUMERIC}, ${3:numRowPerPage NUMERIC}, ${4:isPaged BOOLEAN}, ${5:startRow NUMERIC}, ${6:resetStartRow BOOLEAN}, ${7:btpag STRING}, ${8:[debug] BOOLEAN}})'),
  ('getSOSQLStatement','getSOSQLStatement(${1:${2:column STRING}, ${3:[value] STRING}, ${4:operator NUMERIC}, ${5:so ANY}})'),
  ('listToQuery','listToQuery(${1:${2:id STRING}, ${3:[desc] STRING}, ${4:[idSep] STRING}, ${5:[descSep] STRING}, ${6:[labels] STRUCT}, ${7:[debug] BOOLEAN}, ${8:[idColumnName] STRING}, ${9:[descColumnName] STRING}, ${10:[columntypelist] STRING}})'),
  ('isFirstRecord','isFirstRecord(${1:${2:[query] QUERY}})'),
  ('flex_delete','flex_delete(${1:${2:table_name STRING}, ${3:key ARRAY}, ${4:[name] STRING}, ${5:dbprop STRUCT}, ${6:[debug] BOOLEAN}})'),
  ('queryAddRowWithValue','queryAddRowWithValue(${1:${2:query QUERY}, ${3:[value] STRING}})'),
  ('splitSingleValue','splitSingleValue(${1:${2:str STRING}, ${3:limit NUMERIC}, ${4:[ignoreHTML] BOOLEAN}, ${5:[wordSeparator] STRING}})'),
  ('fixedWidthToQuery','fixedWidthToQuery(${1:${2:columnNames STRING}, ${3:widths STRING}, ${4:data STRING}, ${5:[customRegex] STRING}})'),
  ('queryToXML','queryToXML(${1:${2:[query] }})'),
  ('column_to_string','column_to_string(${1:${2:query QUERY}, ${3:column STRING}, ${4:[separator] STRING}})'),
  ('isLastRecord','isLastRecord(${1:${2:[query] QUERY}})'),
  ('qoqLeftOuterJoin','qoqLeftOuterJoin(${1:${2:queryA QUERY}, ${3:queryB QUERY}, ${4:columnA STRING}, ${5:columnB STRING}, ${6:[datatype] STRING}})'),
  ('query_add_column_from_query','query_add_column_from_query(${1:${2:query_to QUERY}, ${3:query_from QUERY}, ${4:keys ARRAY}, ${5:column_to_add ARRAY}, ${6:[only_match] BOOLEAN}})'),
  ('transformToParentChild','transformToParentChild(${1:${2:query QUERY}, ${3:columns STRING}, ${4:[orderColumns] STRING}, ${5:[rootElementID] STRING}, ${6:[order_type] STRING}})'),
  ('flex_insert','flex_insert(${1:${2:[table_name] STRING}, ${3:[sql_insert] STRING}, ${4:fav ARRAY}, ${5:dbprop STRUCT}, ${6:[debug] BOOLEAN}, ${7:[name] STRING}})'),
  ('QueryToCSVString','QueryToCSVString(${1:${2:queryToCovert QUERY}})'),
  ('querySort','querySort(${1:${2:query QUERY}, ${3:orderBy STRING}})'),
  ('QueryToCSVFile','QueryToCSVFile(${1:${2:queryToCovert QUERY}, ${3:filePath STRING}})'),
  ('queryToStruct','queryToStruct(${1:${2:source QUERY}, ${3:[dest] STRUCT}, ${4:[fields] STRING}, ${5:[source_prefix] STRING}, ${6:[dest_suffix] STRING}, ${7:[numrow] NUMERIC}, ${8:[source_prefix2del] STRING}})'),
  ('duplicateRow','duplicateRow(${1:${2:[query] QUERY}, ${3:[row] NUMERIC}, ${4:[howMany] NUMERIC}})'),
  ('queryToMatrix','queryToMatrix(${1:${2:query QUERY}, ${3:col_x STRING}, ${4:col_y STRING}, ${5:col_value STRING}, ${6:dim_x NUMERIC}, ${7:dim_y NUMERIC}, ${8:[init_value] STRING}, ${9:[debug] BOOLEAN}})'),
  ('flattenQueryOfArrays','flattenQueryOfArrays(${1:${2:query QUERY}})'),
  ('trimQuery','trimQuery(${1:${2:query QUERY}, ${3:[columnlist] STRING}})'),
  ('splitQueryContent','splitQueryContent(${1:${2:query QUERY}, ${3:[maxColumnLength] NUMERIC}, ${4:[ignoreHTML] BOOLEAN}, ${5:[columnOptions] STRUCT}})'),
  ('flex_update','flex_update(${1:${2:table_name STRING}, ${3:key ARRAY}, ${4:fav ARRAY}, ${5:[name] STRING}, ${6:dbprop STRUCT}, ${7:[debug] BOOLEAN}})'),
  ('queryAppend','queryAppend(${1:${2:q1 QUERY}, ${3:q2 QUERY}})'),
  ('flex_search','flex_search(${1:${2:table_name STRING}, ${3:key ARRAY}, ${4:[name] STRING}, ${5:dbprop STRUCT}, ${6:[countOnly] BOOLEAN}, ${7:[maxrows] NUMERIC}, ${8:[columnlist] STRING}, ${9:[orderBy] STRING}, ${10:[debug] BOOLEAN}, ${11:[cacheTimeSpan] ANY}})'),
  ('queryColumnsToStruct','queryColumnsToStruct(${1:${2:[query] }, ${3:[keyColumn] }})'),
  ('extractRows','extractRows(${1:${2:[query] QUERY}, ${3:[startRow] NUMERIC}, ${4:[endRow] NUMERIC}})')
]

dotcompletions['lib_search_fso'] = [
  ('lib_search_fso','lib_search_fso(${1:${2:[target_fso] }, ${3:[fso_type] }, ${4:[start_dir] }})')
]

dotcompletions['lib_show'] = [
  ('show_msg_page','show_msg_page(${1:${2:[title] STRING}, ${3:[msg_lines] ARRAY}, ${4:[dump_lines] BOOLEAN}, ${5:[show_footer_link] BOOLEAN}, ${6:[show_html_header] BOOLEAN}, ${7:[additional_html] STRING}})')
]

dotcompletions['lib_str'] = [
  ('safe_str','safe_str(${1:${2:[str] }})'),
  ('getCData','getCData(${1:${2:[str] STRING}})'),
  ('gzip','gzip()'),
  ('RoundIt','RoundIt(${1:${2:[num] }, ${3:[digits] }})'),
  ('trimList','trimList(${1:${2:[listEl] }})'),
  ('decimalRound','decimalRound(${1:${2:[numberToRound] }, ${3:[numberOfPlaces] }})'),
  ('CSVToArray','CSVToArray(${1:${2:CSV STRING}, ${3:[Delimiter] STRING}, ${4:[Qualifier] STRING}})'),
  ('smart_split','smart_split(${1:${2:str2split STRING}, ${3:[maxlength] NUMERIC}, ${4:[line_sep] STRING}})'),
  ('substituteCharsAt','substituteCharsAt(${1:${2:str STRING}, ${3:pos NUMERIC}, ${4:substStr STRING}, ${5:[preserveLength] BOOLEAN}})'),
  ('remove_multiple_spaces','remove_multiple_spaces(${1:${2:str STRING}})'),
  ('getXMLFieldValue','getXMLFieldValue()'),
  ('capitalize','capitalize(${1:${2:[str] STRING}})'),
  ('listSplit','listSplit(${1:${2:[list] STRING}, ${3:[splitEvery] NUMERIC}, ${4:[delimiters] STRING}})'),
  ('format_dec_number','format_dec_number(${1:${2:NumberToBeFormatted NUMERIC}, ${3:TotalLen NUMERIC}, ${4:DecimalLen NUMERIC}, ${5:[SepOut] STRING}, ${6:[Sign] STRING}})'),
  ('maskParse','maskParse(${1:${2:mask STRING}, ${3:source ANY}, ${4:[rowIndex] NUMERIC}, ${5:[tokenStartStr] STRING}, ${6:[tokenEndStr] STRING}, ${7:[defaultValue] STRING}, ${8:[doEscape] BOOLEAN}})'),
  ('gunzip','gunzip()'),
  ('listTrim','listTrim(${1:${2:list STRING}, ${3:[delimiter] STRING}})'),
  ('XmlImport','XmlImport()'),
  ('getNumbersQuery','getNumbersQuery(${1:${2:[column_name] }, ${3:[from] }, ${4:[to] }})'),
  ('capitalizeAll','capitalizeAll(${1:${2:[str] STRING}, ${3:[separator] STRING}})'),
  ('safe_id','safe_id(${1:${2:the_args STRUCT}, ${3:keys STRING}, ${4:[extra_good_re] STRING}})'),
  ('ListLeft','ListLeft(${1:${2:list STRING}, ${3:numElements NUMERIC}, ${4:[delimiter] STRING}, ${5:[startAtElement] NUMERIC}})'),
  ('NumberFormat_v2','NumberFormat_v2(${1:${2:[number] STRING}, ${3:[Fix] NUMERIC}, ${4:[SepMigliaia] BOOLEAN}, ${5:[SepDecimalChar] STRING}, ${6:[fixed_dec] BOOLEAN}, ${7:[thousandsep] STRING}})'),
  ('splitSearchString','splitSearchString(${1:${2:[searchString] STRING}, ${3:[splitBy] STRING}})'),
  ('getTelephonePrefix','getTelephonePrefix(${1:${2:phone_number STRING}})'),
  ('trimChar','trimChar(${1:${2:string2trim STRING}, ${3:[char2trim] STRING}})'),
  ('safe_menu','safe_menu(${1:${2:args STRUCT}, ${3:keys STRING}})'),
  ('string_to_time','string_to_time(${1:${2:str_time STRING}, ${3:input_format STRING}})'),
  ('format_number','format_number(${1:${2:NumberToBeFormatted NUMERIC}, ${3:IntegerLen NUMERIC}, ${4:DecimalLen NUMERIC}, ${5:[Sep] STRING}, ${6:[viewSign] STRING}, ${7:[charToRepeatString] STRING}})'),
  ('formatJSON','formatJSON(${1:${2:[str] STRING}})'),
  ('remove_multiple_chars','remove_multiple_chars(${1:${2:str STRING}, ${3:char2find STRING}, ${4:char2replace STRING}})'),
  ('padStr','padStr(${1:${2:[string] }, ${3:[char] }, ${4:[number] }})'),
  ('cleanHighAscii','cleanHighAscii(${1:${2:text STRING}})'),
  ('getXMLFieldValues','getXMLFieldValues()'),
  ('string_to_date','string_to_date(${1:${2:str_date STRING}, ${3:input_format STRING}})'),
  ('getExtension','getExtension(${1:${2:[name] }})'),
  ('isEmail','isEmail(${1:${2:str STRING}})'),
  ('listDeleteNoCase','listDeleteNoCase(${1:${2:list STRING}, ${3:value STRING}, ${4:[delimiters] STRING}})'),
  ('REFindAll','REFindAll(${1:${2:regex STRING}, ${3:text STRING}, ${4:[ignoreCase] BOOLEAN}})'),
  ('mask_str','mask_str(${1:${2:str STRING}, ${3:[mask] STRING}, ${4:[mask_dir] STRING}})'),
  ('split','split(${1:${2:str STRING}, ${3:[splitStr] STRING}, ${4:[treatSplitStrAsStr] BOOLEAN}})'),
  ('REEscape','REEscape(${1:${2:[theString] }})'),
  ('string_to_number','string_to_number(${1:${2:str_num STRING}, ${3:[dec_pos] NUMERIC}, ${4:[dec_sep] STRING}, ${5:[info] STRING}})'),
  ('trunc','trunc(${1:${2:[number] }, ${3:[num_dec] }})'),
  ('checkContainerNumber','checkContainerNumber(${1:${2:contNumber STRING}})'),
  ('validateMailList','validateMailList(${1:${2:str STRING}})'),
  ('REFindAllNoCase','REFindAllNoCase(${1:${2:regex STRING}, ${3:text STRING}})'),
  ('lib_masked_id_increment','lib_masked_id_increment(${1:${2:id STRING}, ${3:mask STRING}})'),
  ('getValueFromEAN13','getValueFromEAN13(${1:${2:ean13 STRING}, ${3:[removeTipoCodifica] BOOLEAN}, ${4:[removeCheckDigit] BOOLEAN}})'),
  ('jsondecode','jsondecode(${1:${2:data STRING}, ${3:[debugStructName] STRING}})'),
  ('HTMLSafe','HTMLSafe(${1:${2:[string] }})'),
  ('truncNumber','truncNumber(${1:${2:input NUMERIC}, ${3:[decimals] NUMERIC}})'),
  ('listFix','listFix(${1:${2:list STRING}, ${3:[null_string] STRING}, ${4:[delimiter] STRING}})'),
  ('jsonencode','jsonencode(${1:${2:data ANY}, ${3:[queryFormat] STRING}, ${4:[queryKeyCase] STRING}, ${5:[stringNumbers] BOOLEAN}, ${6:[formatDates] BOOLEAN}, ${7:[columnListFormat] STRING}, ${8:[queryDataOnly] BOOLEAN}, ${9:[structKeyCase] STRING}, ${10:[doEscape] BOOLEAN}})'),
  ('simpleTextParser','simpleTextParser(${1:${2:[str] STRING}, ${3:[keys] STRUCT}, ${4:[tokenStartStr] STRING}, ${5:[tokenEndStr] STRING}})'),
  ('checkPartitaIVA','checkPartitaIVA(${1:${2:partitaIVA STRING}})'),
  ('lib_val','lib_val(${1:${2:[n] }})'),
  ('StripHTML','StripHTML(${1:${2:[str] STRING}, ${3:[tagList] STRING}})'),
  ('generateNumericList','generateNumericList(${1:${2:[from] NUMERIC}, ${3:[to] NUMERIC}, ${4:[step] NUMERIC}})'),
  ('getMaskElements','getMaskElements(${1:${2:mask STRING}, ${3:tokenStart STRING}, ${4:tokenEnd STRING}})'),
  ('randString','randString(${1:${2:type STRING}, ${3:length NUMERIC}})'),
  ('listDelete','listDelete(${1:${2:list STRING}, ${3:value STRING}, ${4:[delimiters] STRING}})'),
  ('lib_importoN','lib_importoN(${1:${2:[num] }, ${3:[len] }})'),
  ('lib_safe_struct_strings','lib_safe_struct_strings(${1:${2:[struct_in] }, ${3:[field_list] }})'),
  ('do_ellipsis','do_ellipsis(${1:${2:the_str STRING}, ${3:char_count NUMERIC}})'),
  ('ListCompare','ListCompare(${1:${2:[List1] }, ${3:[List2] }})'),
  ('listVenn','listVenn(${1:${2:[ListA] }, ${3:[ListB] }, ${4:[ReturnListType] }})')
]

dotcompletions['lib_struct'] = [
  ('populateStructFromStruct','populateStructFromStruct(${1:${2:source STRUCT}, ${3:dest STRUCT}, ${4:[fields] STRING}, ${5:[source_prefix] STRING}, ${6:[dest_prefix] STRING}})'),
  ('structMerge','structMerge(${1:${2:struct1 STRUCT}, ${3:struct2 STRUCT}})'),
  ('structTrim','structTrim(${1:${2:items STRUCT}})'),
  ('CtrlRequiredParam','CtrlRequiredParam(${1:${2:struct_param STRUCT}, ${3:listRequired STRING}, ${4:[allowBlank] BOOLEAN}, ${5:[debug] BOOLEAN}})'),
  ('ConvertXmlToStruct','ConvertXmlToStruct(${1:${2:xmlNode STRING}, ${3:str STRUCT}})'),
  ('convertStructToXml','convertStructToXml(${1:${2:source ANY}, ${3:rootName STRING}})'),
  ('removeEmptyStructureKeys','removeEmptyStructureKeys(${1:${2:structure STRUCT}})'),
  ('duplicate_struct','duplicate_struct(${1:${2:struct_src ANY}, ${3:[debug] BOOLEAN}})'),
  ('init_struct_reg_cat','init_struct_reg_cat(${1:${2:recordset_reg_cat QUERY}, ${3:list_cbo_reg STRING}, ${4:[args_struct] STRUCT}})'),
  ('structBlend','structBlend(${1:${2:Struct1 STRUCT}, ${3:Struct2 STRUCT}})'),
  ('structFilter','structFilter(${1:${2:struct STRUCT}, ${3:[filter] STRING}})'),
  ('structFilterByKeyList','structFilterByKeyList(${1:${2:struct STRUCT}, ${3:keyList STRING}})'),
  ('structReverse','structReverse(${1:${2:structure STRUCT}})'),
  ('structOfStructuresToQuery','structOfStructuresToQuery(${1:${2:theStruct STRUCT}, ${3:primaryKey STRING}})'),
  ('lib_manage_struct','lib_manage_struct(${1:${2:struct_save STRUCT}, ${3:struct_src STRUCT}, ${4:[clear_src] BOOLEAN}})'),
  ('structToList','structToList(${1:${2:s STRUCT}, ${3:[delimiter] STRING}})'),
  ('listToStruct','listToStruct(${1:${2:[list] STRING}, ${3:[delimiter] STRING}, ${4:[internalDelimiter] STRING}, ${5:[defaultValue] STRING}, ${6:[parseStructKey] STRING}, ${7:[listValues] STRING}})'),
  ('getKeys','getKeys(${1:${2:struct STRUCT}, ${3:keys STRING}})'),
  ('getKeysWithPrefix','getKeysWithPrefix(${1:${2:the_struct STRUCT}, ${3:[prefix] STRING}})')
]

dotcompletions['lib_ui'] = [
  ('lib_insert_ico_ele','lib_insert_ico_ele(${1:${2:[struct_name] }})'),
  ('drawColorPicker','drawColorPicker(${1:${2:[box_id] STRING}, ${3:[pagePath] STRING}, ${4:[name] STRING}, ${5:[id] STRING}, ${6:[type] STRING}, ${7:[value] STRING}, ${8:[html_attributes] STRING}, ${9:[linkLabel] STRING}})'),
  ('draw_radio_yn','draw_radio_yn(${1:${2:name STRING}, ${3:selected_value STRING}, ${4:labels STRUCT}, ${5:[html_attributes] STRING}})'),
  ('draw_str_intersoc','draw_str_intersoc(${1:${2:[class_intersoc] }, ${3:[class_privato] }, ${4:[lblobj] }, ${5:[lbl_struct] }})'),
  ('get_msg','get_msg(${1:${2:idmessage STRING}, ${3:idlingua STRING}, ${4:[replace_text] ARRAY}, ${5:[idlingua_default] STRING}, ${6:dbprop STRUCT}, ${7:[debug] BOOLEAN}})'),
  ('draw_form_footer','draw_form_footer(${1:${2:fn_goback STRING}, ${3:[button_help_pathname] STRING}, ${4:[footer_text] STRING}})'),
  ('get_html_opt_transfer','get_html_opt_transfer(${1:${2:obj_from STRUCT}, ${3:obj_to STRUCT}, ${4:[right_list] STRING}, ${5:[disabled] STRING}, ${6:images STRUCT}, ${7:labels STRUCT}, ${8:[debug] BOOLEAN}, ${9:[js_ot_name] STRING}, ${10:[size] NUMERIC}, ${11:[style] STRING}, ${12:[enable_search] BOOLEAN}, ${13:[search_size] NUMERIC}, ${14:[readonly] STRING}, ${15:[show_order] BOOLEAN}, ${16:[initializeOt] BOOLEAN}})'),
  ('padl_query_field','padl_query_field(${1:${2:query QUERY}, ${3:field_counter STRING}, ${4:field_to_change STRING}, ${5:[new_field_name] STRING}, ${6:[html_content] STRING}, ${7:[field_id] STRING}, ${8:[id_to_exclude] STRING}, ${9:[pad_str] STRING}, ${10:[last_pad] STRING}, ${11:[draw_root] BOOLEAN}, ${12:[debug] BOOLEAN}})'),
  ('lib_button_console','lib_button_console(${1:${2:[img_struct] STRUCT}, ${3:[lbl_struct] STRUCT}, ${4:[onclick_var] STRING}, ${5:[enable_fb] STRING}, ${6:[show_wb] STRING}})'),
  ('lib_input_box','lib_input_box(${1:${2:box_def ARRAY}, ${3:args STRUCT}, ${4:[draw_table] BOOLEAN}})'),
  ('lib_search_box','lib_search_box(${1:${2:box_def ARRAY}, ${3:args STRUCT}, ${4:[add_table] BOOLEAN}})'),
  ('lib_control_empty_fields','lib_control_empty_fields(${1:${2:field_msg STRUCT}, ${3:field_to_control STRUCT}})'),
  ('draw_key_lock','draw_key_lock(${1:${2:[label_lock] STRING}, ${3:[label_unlock] STRING}, ${4:[image_lock] STRING}, ${5:[image_unlock] STRING}, ${6:[html_attributes] STRING}, ${7:[id] STRING}})'),
  ('draw_numrange','draw_numrange(${1:${2:[type] STRING}, ${3:name STRING}, ${4:[selected_value] STRING}, ${5:[min_value] NUMERIC}, ${6:[max_value] NUMERIC}, ${7:[step] NUMERIC}, ${8:[add_blank_option] BOOLEAN}, ${9:[blank_option_text] STRING}, ${10:[blank_option_value] STRING}, ${11:[html_attributes] STRING}})'),
  ('lib_insert_ico_transfer','lib_insert_ico_transfer()'),
  ('main_title_table','main_title_table(${1:${2:[message] STRING}, ${3:[tbgcolor] STRING}, ${4:[tclass] STRING}, ${5:[timage] STRUCT}})'),
  ('lib_init_args_stdges','lib_init_args_stdges(${1:${2:[struct_args] }})'),
  ('lib_button_ges','lib_button_ges(${1:${2:[opera] STRING}, ${3:[img_struct] STRUCT}, ${4:[lbl_struct] STRUCT}, ${5:[onclick_var] STRING}, ${6:[drawId] BOOLEAN}})'),
  ('draw_opt_transfer','draw_opt_transfer(${1:${2:obj_from STRUCT}, ${3:obj_to STRUCT}, ${4:[right_list] STRING}, ${5:[disabled] STRING}, ${6:images STRUCT}, ${7:labels STRUCT}, ${8:[debug] BOOLEAN}, ${9:[js_ot_name] STRING}, ${10:[size] NUMERIC}, ${11:[style] STRING}, ${12:[enable_search] BOOLEAN}, ${13:[layout] STRING}, ${14:[search_size] NUMERIC}, ${15:[readonly] STRING}, ${16:[show_order] BOOLEAN}, ${17:[initializeOt] BOOLEAN}})'),
  ('drawOperatorsCbo','drawOperatorsCbo(${1:${2:[name] STRING}, ${3:[value] STRING}, ${4:[operators] STRING}, ${5:[operatorsDesc] STRING}, ${6:[addBlankOption] BOOLEAN}, ${7:[htmlAttributes] STRING}})'),
  ('init','init()'),
  ('lib_init_args_stdele','lib_init_args_stdele()'),
  ('draw_form_link','draw_form_link(${1:${2:[field_name] STRING}, ${3:[field_value] STRING}, ${4:[href_text] STRING}, ${5:[href_cmd] STRING}, ${6:[html_attributes] STRING}})'),
  ('isListInListNoCase','isListInListNoCase(${1:${2:l1 STRING}, ${3:l2 STRING}, ${4:[delim1] STRING}, ${5:[delim2] STRING}, ${6:[matchany] BOOLEAN}})'),
  ('isFullScreen','isFullScreen(${1:${2:[proc] }})'),
  ('drawSectionTitle','drawSectionTitle(${1:${2:target STRING}, ${3:title STRING}, ${4:[titleID] STRING}, ${5:[cssClass] STRING}})'),
  ('translateFileExt','translateFileExt(${1:${2:fileExt STRING}})'),
  ('getAllMessages','getAllMessages(${1:${2:idlingua STRING}, ${3:[idlinguaDefault] STRING}, ${4:dbprop STRUCT}})'),
  ('hackModifica2Salva','hackModifica2Salva(${1:${2:[buttonsData] ARRAY}})'),
  ('draw_hidden_fields','draw_hidden_fields(${1:${2:[field_list] STRING}, ${3:[values] STRUCT}, ${4:[draw_always] BOOLEAN}})'),
  ('lib_show_results','lib_show_results(${1:${2:myQuery QUERY}, ${3:startRow NUMERIC}, ${4:endRow NUMERIC}, ${5:radioName STRING}, ${6:table_cfg ARRAY}, ${7:hilite_color STRING}, ${8:[view_radio] BOOLEAN}, ${9:[title_class] STRING}, ${10:[multiple_field_sep] STRING}})'),
  ('init_all_labels','init_all_labels(${1:${2:id_lingua STRING}, ${3:dbprop STRUCT}, ${4:[id_lingua_default] STRING}})'),
  ('draw_standard_cbo','draw_standard_cbo(${1:${2:cbo_name STRING}, ${3:[opt2sel] STRING}, ${4:[query_obj] QUERY}, ${5:id_field STRING}, ${6:[id_glue] STRING}, ${7:desc_field STRING}, ${8:[desc_glue] STRING}, ${9:[desc_html_content] BOOLEAN}, ${10:[disabled] BOOLEAN}, ${11:[onchange_str] STRING}, ${12:[add_blank_opt] BOOLEAN}, ${13:[blank_opt_value] STRING}, ${14:[blank_opt_desc] STRING}, ${15:[css_class] STRING}, ${16:[show_id_in_desc] BOOLEAN}, ${17:[html_attr] STRING}, ${18:[style_field] STRING}, ${19:[draw_hidden] BOOLEAN}, ${20:[linkedfields] STRUCT}, ${21:[multiple] BOOLEAN}, ${22:[size] NUMERIC}, ${23:[id_group_field] STRING}, ${24:[desc_group_field] STRING}, ${25:[autocomplete] BOOLEAN}, ${26:[autosuggest] BOOLEAN}, ${27:[bind] STRUCT}, ${28:[textFree] BOOLEAN}, ${29:[show_id_in_options] BOOLEAN}, ${30:[opt2prepend] ARRAY}, ${31:[viewResetButton] BOOLEAN}, ${32:[text] STRING}})'),
  ('draw_selectall','draw_selectall(${1:${2:selectbox STRING}, ${3:[label] STRING}, ${4:[html_attributes] STRING}})'),
  ('updateAppMessages','updateAppMessages()'),
  ('draw_req_data','draw_req_data(${1:${2:tge050_data STRUCT}, ${3:lbl_struct STRUCT}, ${4:[debug] BOOLEAN}})'),
  ('lib_html_head','lib_html_head(${1:${2:[css_file] STRING}, ${3:[js_file] STRING}, ${4:[css_print_file] STRING}, ${5:[a_css_files] ARRAY}, ${6:[a_js_files] ARRAY}, ${7:[doctype] STRING}})'),
  ('trad_msg_tablet','trad_msg_tablet(${1:${2:messagelist STRING}, ${3:idlingua STRING}, ${4:dbprop STRUCT}, ${5:[idlingua_default] STRING}, ${6:[js_fn_name] STRING}, ${7:[replace_text] STRUCT}, ${8:[delay] NUMERIC}})'),
  ('draw_query_navbar','draw_query_navbar(${1:${2:[num_records] NUMERIC}, ${3:[curr_row] NUMERIC}, ${4:[url_page] STRING}, ${5:[rows_per_page] NUMERIC}, ${6:[labels] STRUCT}, ${7:[stylesheet] STRING}, ${8:[show_nav_links] BOOLEAN}, ${9:[startrow_name] STRING}, ${10:[idlingua] STRING}})'),
  ('setFocusOn','setFocusOn(${1:${2:element_id STRING}})'),
  ('lib_html_title_goback','lib_html_title_goback(${1:${2:[title] }, ${3:[ico_goback] }, ${4:[alt_ico_goback] }, ${5:[varname] }, ${6:[lbl_campi_obb] }})'),
  ('tr_html_input_text','tr_html_input_text(${1:${2:input STRUCT}, ${3:td STRUCT}})'),
  ('cr_search_sql','cr_search_sql(${1:${2:[q_struct] }, ${3:[args_struct] }})'),
  ('lib_find_not_empty_field','lib_find_not_empty_field(${1:${2:[struct_in] }, ${3:[field_list] }})'),
  ('cbo_reg_cat','cbo_reg_cat(${1:${2:idsocieta STRING}, ${3:proc_cat STRING}, ${4:reg_cat_value STRUCT}, ${5:[table_attributes] STRUCT}, ${6:[td_attributes] STRUCT}, ${7:[add_blank_option] BOOLEAN}, ${8:[show_id_in_desc] BOOLEAN}, ${9:[filter_soc_ruoli] BOOLEAN}, ${10:[session_struct] STRUCT}, ${11:[cbo_name_prefix] STRING}, ${12:[idsocieta_inlinea] STRING}, ${13:[list_cbo_reg_name] STRING}, ${14:[html_attr] STRING}, ${15:[used_for_filter] BOOLEAN}, ${16:q_livelli_regole QUERY}, ${17:[cbo_labels] ARRAY}, ${18:[layout] STRING}, ${19:[viewFilterCbo] BOOLEAN}, ${20:[showCboLivelli] STRING}, ${21:dbprop STRUCT}, ${22:[debug] BOOLEAN}})'),
  ('lib_html_body','lib_html_body()'),
  ('draw_cbo_valuta','draw_cbo_valuta(${1:${2:name STRING}, ${3:query QUERY}, ${4:[selected_value] STRING}, ${5:[html_attributes] STRING}, ${6:[draw_desc] BOOLEAN}})'),
  ('translate_labels','translate_labels(${1:${2:labelProp STRUCT}, ${3:[get_all] BOOLEAN}, ${4:id_lingua STRING}, ${5:dbprop STRUCT}})'),
  ('draw_cbo_anag','draw_cbo_anag(${1:${2:name STRING}, ${3:query QUERY}, ${4:[use_filter] BOOLEAN}, ${5:[selected_value] STRING}, ${6:[html_attributes] STRING}, ${7:[view_id] BOOLEAN}})'),
  ('draw_currency_symbol','draw_currency_symbol(${1:${2:glb_struct }, ${3:dbprop }, ${4:[debug] }})'),
  ('drawAutoSuggest','drawAutoSuggest(${1:${2:id STRING}, ${3:[name] STRING}, ${4:[value] STRING}, ${5:[descvalue] STRING}, ${6:[maxlength] NUMERIC}, ${7:[MinCharToStartSearch] NUMERIC}, ${8:[disabled] BOOLEAN}})'),
  ('write_id_desc','write_id_desc(${1:${2:id STRING}, ${3:desc STRING}, ${4:[html_content] BOOLEAN}})'),
  ('drawRuler','drawRuler(${1:${2:[cols] NUMERIC}, ${3:[trClass] STRING}, ${4:[fillString] STRING}})'),
  ('write_duration_time','write_duration_time(${1:${2:seconds NUMERIC}, ${3:cfg_struct STRUCT}, ${4:[labels] STRUCT}, ${5:[readonly] BOOLEAN}, ${6:[only_text] BOOLEAN}})'),
  ('lib_html_hidden_prefix','lib_html_hidden_prefix(${1:${2:[struct_in] }, ${3:[prefix] }})'),
  ('lib_viewer_ges','lib_viewer_ges(${1:${2:[input_box_cfg] }, ${3:[struct_args] }, ${4:[struct_colors] }, ${5:[struct_img] }, ${6:[struct_lbl] }, ${7:[operation] }, ${8:[var_name_opera] }, ${9:[title] }, ${10:[ico_goback] }, ${11:[lbl_ico_goback] }, ${12:[lbl_campi_obb] }})'),
  ('get_labels','get_labels(${1:${2:idlingua STRING}})'),
  ('lib_button_goback','lib_button_goback(${1:${2:[href] }, ${3:[url_struct] }, ${4:[session_struct] }, ${5:[img] }, ${6:[alt] }})'),
  ('init_labels','init_labels(${1:${2:session_struct STRUCT}})'),
  ('getGradientColors','getGradientColors(${1:${2:[colorA] }, ${3:[colorB] }, ${4:[steps] }})'),
  ('draw_form_title','draw_form_title(${1:${2:[fn_goback] }, ${3:[title] }, ${4:[lbl_obb_fields] }})'),
  ('drawNumericField','drawNumericField(${1:${2:id STRING}, ${3:[name] STRING}, ${4:[value] STRING}, ${5:numint NUMERIC}, ${6:[numdec] NUMERIC}, ${7:[defaultvalue] STRING}, ${8:[allowzero] BOOLEAN}, ${9:[allowsigned] BOOLEAN}, ${10:[disabled] BOOLEAN}, ${11:[readonly] BOOLEAN}, ${12:[onfocus] STRING}, ${13:[onchange] STRING}, ${14:[onblur] STRING}, ${15:[addclass] STRING}, ${16:[msgerr] STRING}, ${17:[htmlAttributes] STRING}, ${18:[formatWhenDisabled] BOOLEAN}, ${19:[applyFormatting] BOOLEAN}})'),
  ('lib_html_url_prefix','lib_html_url_prefix(${1:${2:struct_in STRUCT}, ${3:[prefix] STRING}})'),
  ('trad_msg','trad_msg(${1:${2:messagelist ANY}, ${3:idlingua STRING}, ${4:dbprop STRUCT}, ${5:[idlingua_default] STRING}, ${6:[js_fn_name] STRING}, ${7:[replace_text] STRUCT}, ${8:[delay] NUMERIC}, ${9:[retOnlyMsg] BOOLEAN}})'),
  ('drawPageButtons','drawPageButtons(${1:${2:[buttonsData] ARRAY}, ${3:[containerID] STRING}, ${4:[containerAttributes] STRING}, ${5:[cmdFieldName] STRING}, ${6:[usePermissions] BOOLEAN}, ${7:labels STRUCT}, ${8:images STRUCT}, ${9:[my_session] STRUCT}, ${10:[viewMissingLabels] BOOLEAN}, ${11:[alwaysVisibleButtons] STRING}, ${12:[viewLabels] BOOLEAN}, ${13:[buttonsLayout] STRING}})'),
  ('update_app_label','update_app_label(${1:${2:const STRUCT}})')
]

dotcompletions['lib_url'] = [
  ('url_qs_to_struct','url_qs_to_struct(${1:${2:url_query_string STRING}})'),
  ('rdslash','rdslash(${1:${2:stringads STRING}, ${3:[debug] BOOLEAN}})'),
  ('safe_url_qs','safe_url_qs(${1:${2:[url_query_string] STRING}})'),
  ('url2path','url2path(${1:${2:idsocieta STRING}, ${3:idregarch STRING}, ${4:url STRING}, ${5:webserver_url STRING}, ${6:dbprop STRUCT}})'),
  ('gen_url_qs_prefix','gen_url_qs_prefix(${1:${2:args_struct STRUCT}, ${3:[search_field_prefix] STRING}})'),
  ('url_maker','url_maker(${1:${2:mycgi STRUCT}, ${3:[port] STRING}})')
]

class DotCompletionsCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        sel = self.view.sel()[0]

        # insert the actual . character
        for region in self.view.sel():
            self.view.insert(edit, region.end(), '.')

        if self.view.settings().get('auto_complete') == False:
            return

        word = self.view.word(sel.begin() - 1)

        completions.extend(dotcompletions[self.view.substr(word)])
        t = self.view.settings().get('auto_complete_delay')
        sublime.set_timeout(lambda:
                self.view.run_command('auto_complete', {
                                    'disable_auto_insert': True,
                                    'next_completion_if_showing': False,
                                    'api_completions_only': True}), t)

class OnDotCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        _completions = []
        _completions.extend(completions)

        del completions[:]
        return _completions

