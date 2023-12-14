-- Select and rank Glam rock bands based on their longevity
SELECT
    band_name,
    FLOOR((YEAR('2022-01-01') - formed) / 10) * 10 AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC, band_name;