SELECT cadastralnum
FROM bufferbase JOIN listforrating
                ON listforrating_unid = listforrating.unid AND
                   listforrating.valuationdate = %(date)s
ORDER BY cadastralnum