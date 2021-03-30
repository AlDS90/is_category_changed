SELECT cadastralnum,
       cadastralblock,
       groupid,
       codecalcuse,
       codeuse,
       listforrating.name as name,
       valuationdate as date,
       areasdisplay,
       utilizationbydoc,
       note
FROM bufferbase JOIN listforrating
                ON listforrating_unid = listforrating.unid AND
                   listforrating.valuationdate <= %(date)s
WHERE cadastralnum IN (%(kns)s)
ORDER BY cadastralnum, date DESC