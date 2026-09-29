-- ========================================
-- VIEW - PIPELINE IOT - CORRIGIDO
-- ========================================

CREATE OR REPLACE VIEW vw_temperature_readings AS
SELECT
    id,
    room_id,
    noted_date,
    temp,
    out_in
FROM temperature_readings;

CREATE OR REPLACE VIEW vw_avg_temp_por_sala AS
SELECT
    room_id,
    AVG(temp) as media_temperatura,
    COUNT(*) as total_leituras
FROM temperature_readings
GROUP BY room_id;

CREATE OR REPLACE VIEW vw_temp_por_dia AS
SELECT
    DATE(noted_date) as dia,
    AVG(temp) as media_dia,
    MAX(temp) as max_temp,
    MIN(temp) as min_temp
FROM temperature_readings
GROUP BY DATE(noted_date)
ORDER BY dia;

CREATE OR REPLACE VIEW vw_in_out AS
SELECT
    out_in,
    AVG(temp) as media_temp,
    COUNT(*) as total
FROM temperature_readings
GROUP BY out_in;