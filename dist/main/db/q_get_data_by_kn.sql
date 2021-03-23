SELECT cadastralnum,
       cadastralblock,
       listforrating.name as name,
       valuationdate as date,
       areasdisplay,
       utilizationbydoc,
       note
FROM bufferbase JOIN listforrating
                ON listforrating_unid = listforrating.unid AND
                   listforrating.valuationdate <= %(date)s
WHERE cadastralnum IN (%(kn)s)
ORDER BY cadastralnum, date DESC