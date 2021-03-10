SELECT cadastralnum,
       listforrating.name as name,
       valuationdate as date
FROM bufferbase JOIN listforrating
                ON listforrating_unid = listforrating.unid AND
                   listforrating.valuationdate = %(date)s
ORDER BY cadastralnum