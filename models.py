QUERY_FCT = """WITH equivalent_store AS (
    SELECT 'CABECERA (322)' store_desc, 2 line_fct, 322 id_fct, 1 line_jano, 322 id_jano UNION ALL
    SELECT 'E_COMMERCE (204)' store_desc, 3 line_fct, 204 id_fct, 1 line_jano, 204 id_jano UNION ALL
    SELECT 'EASY 4SUR MEDELLIN (3814)' store_desc, 4 line_fct, 3814 id_fct, 2 line_jano, 814 id_jano UNION ALL
    SELECT 'EASY ALTOS DEL PRADO (3043)' store_desc, 4 line_fct, 3043 id_fct, 2 line_jano, 43 id_jano UNION ALL
    SELECT 'EASY AMERICAS (5)' store_desc, 4 line_fct, 5 id_fct, 2 line_jano, 802 id_jano UNION ALL
    SELECT 'EASY AUTOSUR (1006)' store_desc, 4 line_fct, 1006 id_fct, 2 line_jano, 18 id_jano UNION ALL
    SELECT 'EASY BOSA (1002)' store_desc, 4 line_fct, 1002 id_fct, 2 line_jano, 10 id_jano UNION ALL
    SELECT 'EASY CALLE 13 (3811)' store_desc, 4 line_fct, 3811 id_fct, 2 line_jano, 811 id_jano UNION ALL
    SELECT 'EASY CALLE 170 (3014)' store_desc, 4 line_fct, 3014 id_fct, 2 line_jano, 14 id_jano UNION ALL
    SELECT 'EASY CALLE 80 (1004)' store_desc, 4 line_fct, 1004 id_fct, 2 line_jano, 11 id_jano UNION ALL
    SELECT 'EASY CENTRO MAYOR (3805)' store_desc, 4 line_fct, 3805 id_fct, 2 line_jano, 805 id_jano UNION ALL
    SELECT 'EASY GAITAN CORTES (3813)' store_desc, 4 line_fct, 3813 id_fct, 2 line_jano, 813 id_jano UNION ALL
    SELECT 'EASY HAYUELOS (12)' store_desc, 4 line_fct, 12 id_fct, 2 line_jano, 15 id_jano UNION ALL
    SELECT 'EASY MAYALES VALLEDUPAR (3809)' store_desc, 4 line_fct, 3809 id_fct, 2 line_jano, 809 id_jano UNION ALL
    SELECT 'EASY NORTE (3801)' store_desc, 4 line_fct, 3801 id_fct, 2 line_jano, 801 id_jano UNION ALL
    SELECT 'EASY OCCIDENTE (3800)' store_desc, 4 line_fct, 3800 id_fct, 2 line_jano, 800 id_jano UNION ALL
    SELECT 'EASY PRADO MEDELLIN (3806)' store_desc, 4 line_fct, 3806 id_fct, 2 line_jano, 806 id_jano UNION ALL
    SELECT 'EASY SOACHA (3812)' store_desc, 4 line_fct, 3812 id_fct, 2 line_jano, 812 id_jano UNION ALL
    SELECT 'EDS 1 MAYO (8)' store_desc, 3 line_fct, 8 id_fct, 1 line_jano, 8 id_jano UNION ALL
    SELECT 'EDS ALAMOS (139)' store_desc, 3 line_fct, 139 id_fct, 1 line_jano, 139 id_jano UNION ALL
    SELECT 'EDS ALQUERIA (149)' store_desc, 3 line_fct, 149 id_fct, 1 line_jano, 149 id_jano UNION ALL
    SELECT 'EDS APOLO AUTOSUR (21)' store_desc, 3 line_fct, 21 id_fct, 1 line_jano, 21 id_jano UNION ALL
    SELECT 'EDS AV DEL RIO (98)' store_desc, 3 line_fct, 98 id_fct, 1 line_jano, 98 id_jano UNION ALL
    SELECT 'EDS AVD CIUDAD CALI (145)' store_desc, 3 line_fct, 145 id_fct, 1 line_jano, 145 id_jano UNION ALL
    SELECT 'EDS BAHIA CL 46 (136)' store_desc, 3 line_fct, 136 id_fct, 1 line_jano, 136 id_jano UNION ALL
    SELECT 'EDS CALLE 190 (161)' store_desc, 3 line_fct, 161 id_fct, 1 line_jano, 161 id_jano UNION ALL
    SELECT 'EDS COLOMBIA CALLE 50 (7)' store_desc, 3 line_fct, 7 id_fct, 1 line_jano, 7 id_jano UNION ALL
    SELECT 'EDS IVESUR CIRCUN (123)' store_desc, 3 line_fct, 123 id_fct, 1 line_jano, 123 id_jano UNION ALL
    SELECT 'EDS LA 17 CRA 17 (159)' store_desc, 3 line_fct, 159 id_fct, 1 line_jano, 159 id_jano UNION ALL
    SELECT 'EDS LA 24 CL 5B (132)' store_desc, 3 line_fct, 132 id_fct, 1 line_jano, 132 id_jano UNION ALL
    SELECT 'EDS LA 42 CL 34B (158)' store_desc, 3 line_fct, 158 id_fct, 1 line_jano, 158 id_jano UNION ALL
    SELECT 'EDS MARRUECOS (2)' store_desc, 3 line_fct, 2 id_fct, 1 line_jano, 2 id_jano UNION ALL
    SELECT 'EDS SAN GABRIEL AERO (133)' store_desc, 3 line_fct, 133 id_fct, 1 line_jano, 133 id_jano UNION ALL
    SELECT 'EDS SEVILLANA (146)' store_desc, 3 line_fct, 146 id_fct, 1 line_jano, 146 id_jano UNION ALL
    SELECT 'EDS SIMON BOLIVAR CL 25 (134)' store_desc, 3 line_fct, 134 id_fct, 1 line_jano, 134 id_jano UNION ALL
    SELECT 'EDS SOACHA TERRENOS (160)' store_desc, 3 line_fct, 160 id_fct, 1 line_jano, 160 id_jano UNION ALL
    SELECT 'EDS TERCERA CL 34 (125)' store_desc, 3 line_fct, 125 id_fct, 1 line_jano, 125 id_jano UNION ALL
    SELECT 'EDS TINTALITO (101)' store_desc, 3 line_fct, 101 id_fct, 1 line_jano, 101 id_jano UNION ALL
    SELECT 'EDS TREBOL CL 76 (121)' store_desc, 3 line_fct, 121 id_fct, 1 line_jano, 121 id_jano UNION ALL
    SELECT 'EDS YUMBO CRA 33 (102)' store_desc, 3 line_fct, 102 id_fct, 1 line_jano, 102 id_jano UNION ALL
    SELECT 'JUMBO 20 DE JULIO (17)' store_desc, 2 line_fct, 17 id_fct, 1 line_jano, 17 id_jano UNION ALL
    SELECT 'JUMBO ALTOS DEL COUNTRY (249)' store_desc, 1 line_fct, 249 id_fct, 1 line_jano, 249 id_jano UNION ALL
    SELECT 'JUMBO ALTOS DEL PRADO (43)' store_desc, 1 line_fct, 43 id_fct, 1 line_jano, 43 id_jano UNION ALL
    SELECT 'JUMBO AMERICANO (86)' store_desc, 1 line_fct, 86 id_fct, 1 line_jano, 86 id_jano UNION ALL
    SELECT 'JUMBO ATLANTIS (194)' store_desc, 1 line_fct, 194 id_fct, 1 line_jano, 194 id_jano UNION ALL
    SELECT 'JUMBO ATRIO (253)' store_desc, 1 line_fct, 253 id_fct, 1 line_jano, 253 id_jano UNION ALL
    SELECT 'JUMBO AUTOPISTA SUR (18)' store_desc, 1 line_fct, 18 id_fct, 1 line_jano, 18 id_jano UNION ALL
    SELECT 'JUMBO BUENAVISTA (88)' store_desc, 1 line_fct, 88 id_fct, 1 line_jano, 88 id_jano UNION ALL
    SELECT 'JUMBO BULEVAR NIZA (3)' store_desc, 1 line_fct, 3 id_fct, 1 line_jano, 3 id_jano UNION ALL
    SELECT 'JUMBO CABECERA (103)' store_desc, 1 line_fct, 103 id_fct, 1 line_jano, 103 id_jano UNION ALL
    SELECT 'JUMBO CALLE 170 (14)' store_desc, 1 line_fct, 14 id_fct, 1 line_jano, 14 id_jano UNION ALL
    SELECT 'JUMBO CALLE 80 (11)' store_desc, 1 line_fct, 11 id_fct, 1 line_jano, 11 id_jano UNION ALL
    SELECT 'JUMBO CANAVERALL (108)' store_desc, 1 line_fct, 108 id_fct, 1 line_jano, 108 id_jano UNION ALL
    SELECT 'JUMBO CARIBE PLAZA (83)' store_desc, 1 line_fct, 83 id_fct, 1 line_jano, 83 id_jano UNION ALL
    SELECT 'JUMBO CARRERA 30 (16)' store_desc, 1 line_fct, 16 id_fct, 1 line_jano, 16 id_jano UNION ALL
    SELECT 'JUMBO CHIA (44)' store_desc, 1 line_fct, 44 id_fct, 1 line_jano, 44 id_jano UNION ALL
    SELECT 'JUMBO CHIA BAZAR (191)' store_desc, 1 line_fct, 191 id_fct, 1 line_jano, 191 id_jano UNION ALL
    SELECT 'JUMBO CHIPICHAPE (31)' store_desc, 1 line_fct, 31 id_fct, 1 line_jano, 31 id_jano UNION ALL
    SELECT 'JUMBO DE LA 65 (23)' store_desc, 1 line_fct, 23 id_fct, 1 line_jano, 23 id_jano UNION ALL
    SELECT 'JUMBO EL CASTILLO (174)' store_desc, 1 line_fct, 174 id_fct, 1 line_jano, 174 id_jano UNION ALL
    SELECT 'JUMBO GIRARDOT (47)' store_desc, 1 line_fct, 47 id_fct, 1 line_jano, 47 id_jano UNION ALL
    SELECT 'JUMBO GUATAPURI (87)' store_desc, 1 line_fct, 87 id_fct, 1 line_jano, 87 id_jano UNION ALL
    SELECT 'JUMBO HAYUELOS (15)' store_desc, 1 line_fct, 15 id_fct, 1 line_jano, 15 id_jano UNION ALL
    SELECT 'JUMBO LAS VEGAS (22)' store_desc, 1 line_fct, 22 id_fct, 1 line_jano, 22 id_jano UNION ALL
    SELECT 'JUMBO LIMONAR PREMIER (30)' store_desc, 1 line_fct, 30 id_fct, 1 line_jano, 30 id_jano UNION ALL
    SELECT 'JUMBO MEGA MALL (84)' store_desc, 1 line_fct, 84 id_fct, 1 line_jano, 84 id_jano UNION ALL
    SELECT 'JUMBO PASTO (128)' store_desc, 2 line_fct, 128 id_fct, 1 line_jano, 128 id_jano UNION ALL
    SELECT 'JUMBO PLAZA CENTRAL (193)' store_desc, 1 line_fct, 193 id_fct, 1 line_jano, 193 id_jano UNION ALL
    SELECT 'JUMBO POPAYAN (36)' store_desc, 1 line_fct, 36 id_fct, 1 line_jano, 36 id_jano UNION ALL
    SELECT 'JUMBO PREMIUM PLAZA (24)' store_desc, 1 line_fct, 24 id_fct, 1 line_jano, 24 id_jano UNION ALL
    SELECT 'JUMBO RIONEGRO (27)' store_desc, 1 line_fct, 27 id_fct, 1 line_jano, 27 id_jano UNION ALL
    SELECT 'JUMBO SAN SILVESTRE (126)' store_desc, 1 line_fct, 126 id_fct, 1 line_jano, 126 id_jano UNION ALL
    SELECT 'JUMBO SANTA ANA (19)' store_desc, 1 line_fct, 19 id_fct, 1 line_jano, 19 id_jano UNION ALL
    SELECT 'JUMBO SANTA FE (72)' store_desc, 1 line_fct, 72 id_fct, 1 line_jano, 72 id_jano UNION ALL
    SELECT 'JUMBO SANTA MARTA (45)' store_desc, 1 line_fct, 45 id_fct, 1 line_jano, 45 id_jano UNION ALL
    SELECT 'JUMBO SANTAFE (148)' store_desc, 1 line_fct, 148 id_fct, 1 line_jano, 148 id_jano UNION ALL
    SELECT 'JUMBO SOACHA (48)' store_desc, 2 line_fct, 48 id_fct, 1 line_jano, 48 id_jano UNION ALL
    SELECT 'JUMBO SUBA (70)' store_desc, 1 line_fct, 70 id_fct, 1 line_jano, 70 id_jano UNION ALL
    SELECT 'JUMBO TITAN (167)' store_desc, 1 line_fct, 167 id_fct, 1 line_jano, 167 id_jano UNION ALL
    SELECT 'JUMBO TUNJA (76)' store_desc, 1 line_fct, 76 id_fct, 1 line_jano, 76 id_jano UNION ALL
    SELECT 'JUMBO UNICENTRO (9)' store_desc, 1 line_fct, 9 id_fct, 1 line_jano, 9 id_jano UNION ALL
    SELECT 'JUMBO VALLE DE LILI (13)' store_desc, 1 line_fct, 13 id_fct, 1 line_jano, 13 id_jano UNION ALL
    SELECT 'JUMBO YOPAL (185)' store_desc, 1 line_fct, 185 id_fct, 1 line_jano, 185 id_jano UNION ALL
    SELECT 'METRO FATELARES (806)' store_desc, 2 line_fct, 806 id_fct, 1 line_jano, 806 id_jano UNION ALL
    SELECT 'METRO FONTIBON (78)' store_desc, 2 line_fct, 78 id_fct, 1 line_jano, 78 id_jano UNION ALL
    SELECT 'METRO MAYALES (184)' store_desc, 2 line_fct, 184 id_fct, 1 line_jano, 184 id_jano UNION ALL
    SELECT 'METRO ALQUERIA (124)' store_desc, 2 line_fct, 124 id_fct, 1 line_jano, 124 id_jano UNION ALL
    SELECT 'METRO ATALAYAS (82)' store_desc, 2 line_fct, 82 id_fct, 1 line_jano, 82 id_jano UNION ALL
    SELECT 'METRO BANDERAS (26)' store_desc, 2 line_fct, 26 id_fct, 1 line_jano, 26 id_jano UNION ALL
    SELECT 'METRO BELLO ANTIOQUIA (25)' store_desc, 2 line_fct, 25 id_fct, 1 line_jano, 25 id_jano UNION ALL
    SELECT 'METRO BOSA (10)' store_desc, 2 line_fct, 10 id_fct, 1 line_jano, 10 id_jano UNION ALL
    SELECT 'METRO BUGA (35)' store_desc, 2 line_fct, 35 id_fct, 1 line_jano, 35 id_jano UNION ALL
    SELECT 'METRO CARTAGO (33)' store_desc, 2 line_fct, 33 id_fct, 1 line_jano, 33 id_jano UNION ALL
    SELECT 'METRO DOSQUEBRADAS (166)' store_desc, 2 line_fct, 166 id_fct, 1 line_jano, 166 id_jano UNION ALL
    SELECT 'METRO DUITAMA (28)' store_desc, 2 line_fct, 28 id_fct, 1 line_jano, 28 id_jano UNION ALL
    SELECT 'METRO E_COMMERCE (203)' store_desc, 3 line_fct, 203 id_fct, 1 line_jano, 203 id_jano UNION ALL
    SELECT 'METRO EXPRESS ALHAMBRA (334)' store_desc, 2 line_fct, 334 id_fct, 1 line_jano, 334 id_jano UNION ALL
    SELECT 'METRO EXPRESS ANT COUNTRY (305)' store_desc, 2 line_fct, 305 id_fct, 1 line_jano, 305 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 125 (340)' store_desc, 2 line_fct, 340 id_fct, 1 line_jano, 340 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 148 (329)' store_desc, 2 line_fct, 329 id_fct, 1 line_jano, 329 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 45 (309)' store_desc, 2 line_fct, 309 id_fct, 1 line_jano, 309 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 93 (324)' store_desc, 2 line_fct, 324 id_fct, 1 line_jano, 324 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 95 (303)' store_desc, 2 line_fct, 303 id_fct, 1 line_jano, 303 id_jano UNION ALL
    SELECT 'METRO EXPRESS CARACAS CON 49 (304)' store_desc, 2 line_fct, 304 id_fct, 1 line_jano, 304 id_jano UNION ALL
    SELECT 'METRO EXPRESS CARRERA 3 (336)' store_desc, 2 line_fct, 336 id_fct, 1 line_jano, 336 id_jano UNION ALL
    SELECT 'METRO EXPRESS CEDRITOS CALL (301)' store_desc, 2 line_fct, 301 id_fct, 1 line_jano, 301 id_jano UNION ALL
    SELECT 'METRO EXPRESS CIUDAD SALITRE (337)' store_desc, 2 line_fct, 337 id_fct, 1 line_jano, 337 id_jano UNION ALL
    SELECT 'METRO EXPRESS CORFERIAS (333)' store_desc, 2 line_fct, 333 id_fct, 1 line_jano, 333 id_jano UNION ALL
    SELECT 'METRO EXPRESS JAVERIANA 45 (335)' store_desc, 2 line_fct, 335 id_fct, 1 line_jano, 335 id_jano UNION ALL
    SELECT 'METRO FACATATIVA (74)' store_desc, 2 line_fct, 74 id_fct, 1 line_jano, 74 id_jano UNION ALL
    SELECT 'METRO FLORIDABLANCA (34)' store_desc, 2 line_fct, 34 id_fct, 1 line_jano, 34 id_jano UNION ALL
    SELECT 'METRO GIRON (39)' store_desc, 2 line_fct, 39 id_fct, 1 line_jano, 39 id_jano UNION ALL
    SELECT 'METRO IBAGUE (42)' store_desc, 2 line_fct, 42 id_fct, 1 line_jano, 42 id_jano UNION ALL
    SELECT 'METRO ITAGUI (46)' store_desc, 2 line_fct, 46 id_fct, 1 line_jano, 46 id_jano UNION ALL
    SELECT 'METRO LA 70 (32)' store_desc, 2 line_fct, 32 id_fct, 1 line_jano, 32 id_jano UNION ALL
    SELECT 'METRO LIBERTADORES (80)' store_desc, 2 line_fct, 80 id_fct, 1 line_jano, 80 id_jano UNION ALL
    SELECT 'METRO MONTERIA (85)' store_desc, 2 line_fct, 85 id_fct, 1 line_jano, 85 id_jano UNION ALL
    SELECT 'METRO MOSQUERA (73)' store_desc, 2 line_fct, 73 id_fct, 1 line_jano, 73 id_jano UNION ALL
    SELECT 'METRO NEIVA (38)' store_desc, 2 line_fct, 38 id_fct, 1 line_jano, 38 id_jano UNION ALL
    SELECT 'METRO PALMIRA (6)' store_desc, 2 line_fct, 6 id_fct, 1 line_jano, 6 id_jano UNION ALL
    SELECT 'METRO PASTO UNICO (171)' store_desc, 2 line_fct, 171 id_fct, 1 line_jano, 171 id_jano UNION ALL
    SELECT 'METRO PITALITO (179)' store_desc, 2 line_fct, 179 id_fct, 1 line_jano, 179 id_jano UNION ALL
    SELECT 'METRO RIOHACHA (40)' store_desc, 2 line_fct, 40 id_fct, 1 line_jano, 40 id_jano UNION ALL
    SELECT 'METRO SAN CAYETANO (79)' store_desc, 2 line_fct, 79 id_fct, 1 line_jano, 79 id_jano UNION ALL
    SELECT 'METRO SAN GIL (183)' store_desc, 2 line_fct, 183 id_fct, 1 line_jano, 183 id_jano UNION ALL
    SELECT 'METRO SANTA LUCIA (195)' store_desc, 2 line_fct, 195 id_fct, 1 line_jano, 195 id_jano UNION ALL
    SELECT 'METRO SIMON BOLIVAR (75)' store_desc, 2 line_fct, 75 id_fct, 1 line_jano, 75 id_jano UNION ALL
    SELECT 'METRO SOGAMOSO (97)' store_desc, 2 line_fct, 97 id_fct, 1 line_jano, 97 id_jano UNION ALL
    SELECT 'METRO TINTALITO (71)' store_desc, 2 line_fct, 71 id_fct, 1 line_jano, 71 id_jano UNION ALL
    SELECT 'METRO VENTURA (81)' store_desc, 2 line_fct, 81 id_fct, 1 line_jano, 81 id_jano UNION ALL
    SELECT 'METRO ZIPAQUIRA (77)' store_desc, 2 line_fct, 77 id_fct, 1 line_jano, 77 id_jano
), droped_e_doc AS (
    SELECT
        ef.num_doc_fact_elec invoice,
        n.num_doc_fact_elec note,
        (ef.vt_factura = n.vt_factura) eq,
        n.codigo_tienda,
        n.nro_terminal,
        n.cod_prov,
        ef.fec_fact invoice_date,
        n.fec_fact note_date
    FROM
        factura.estado_fact_electronica efe
            INNER JOIN factura.encabezado_factura ef ON (
            efe.encfactura_id = ef.encfactura_col_id
                AND efe.estado_dian = 'OK'
            )
            INNER JOIN factura.encabezado_factura n ON (
            ef.num_doc_fact_elec = n.nro_factura_afec
                AND ef.codigo_tienda = n.codigo_tienda
                AND ef.nro_terminal = n.nro_terminal
                AND ef.cod_prov = n.cod_prov
            )
    WHERE
        ef.fec_fact BETWEEN '{start_date} 00:00:00.000' AND '{end_date} 23:59:59.999'
    GROUP BY
        ef.num_doc_fact_elec,
        n.num_doc_fact_elec,
        (ef.vt_factura = n.vt_factura),
        n.codigo_tienda,
        n.nro_terminal,
        n.cod_prov,
        ef.fec_fact,
        n.fec_fact
    HAVING
        (ef.vt_factura = n.vt_factura) IS TRUE
)
SELECT DISTINCT
    ef.encfactura_col_id::VARCHAR id_fct,
    ef.c_origen::VARCHAR,
    SUBSTRING(ef.num_doc_fact_elec, 1, 4) prefijo_fct,
    SUBSTRING(ef.num_doc_fact_elec, 4) consecutivo_fct,
    ef.num_doc_fact_elec factura_fct,
    ef.nro_factura_afec,
    es.line_jano::VARCHAR line_fct,
    es.store_desc tienda_desc_fct,
    es.id_fct::VARCHAR tienda_fct,
    REGEXP_REPLACE(ef.nro_terminal, '^0+', '') caja_fct,
    ef.cod_prov::VARCHAR trx_fct,
    ef.fec_fact::DATE fecha_fct,
    EXTRACT(MONTH FROM efe.f_envio_dian)::VARCHAR mes,
    CASE
        WHEN ef.c_origen IN (4, 9) THEN '-' || ef.vt_factura::INT8::VARCHAR
        ELSE ef.vt_factura::INT8::VARCHAR
    END valor_fct,
    ef.nit_prov::VARCHAR cliente_fct,
    ef.factura_duplicada duplicada,
    efe.f_envio_dian::DATE,
    efe.estado_dian,
    efe.log_errores_dian,
    efe.cufe
FROM
    factura.estado_fact_electronica efe
        INNER JOIN factura.encabezado_factura ef ON (
        efe.encfactura_id = ef.encfactura_col_id
            AND efe.estado_dian = 'OK'
        )
        INNER JOIN equivalent_store es ON (
        ef.codigo_tienda = es.id_fct
        )
        LEFT JOIN droped_e_doc ded ON (
        ef.codigo_tienda = ded.codigo_tienda
            AND ef.nro_terminal = ded.nro_terminal
            AND ef.cod_prov = ded.cod_prov
            AND (ef.num_doc_fact_elec = ded.invoice OR ef.num_doc_fact_elec = ded.note)
        )
WHERE
    ef.fec_fact BETWEEN '{start_date} 00:00:00.000' AND '{end_date} 23:59:59.999'
  AND es.id_fct IN ({stores}) -- NEW
  AND ef.factura_duplicada IS NULL
  AND ded.invoice IS NULL
  AND ef.tip_doc NOT IN (12174, 12170, 5259, 12249, 5427, 5428)
  AND es.line_fct IN (1, 2, 3, 4)
  AND efe.cufe IS NOT NULL
"""


QUERY_JAN = """WITH equivalent_store AS (
    SELECT 'CABECERA (322)' store_desc, 2 line_fct, 322 id_fct, 1 line_jano, 322 id_jano FROM DUAL UNION ALL
    SELECT 'E_COMMERCE (204)' store_desc, 3 line_fct, 204 id_fct, 1 line_jano, 204 id_jano FROM DUAL UNION ALL
    SELECT 'EASY 4SUR MEDELLIN (3814)' store_desc, 4 line_fct, 3814 id_fct, 2 line_jano, 814 id_jano FROM DUAL UNION ALL
    SELECT 'EASY ALTOS DEL PRADO (3043)' store_desc, 4 line_fct, 3043 id_fct, 2 line_jano, 43 id_jano FROM DUAL UNION ALL
    SELECT 'EASY AMERICAS (5)' store_desc, 4 line_fct, 5 id_fct, 2 line_jano, 802 id_jano FROM DUAL UNION ALL
    SELECT 'EASY AUTOSUR (1006)' store_desc, 4 line_fct, 1006 id_fct, 2 line_jano, 18 id_jano FROM DUAL UNION ALL
    SELECT 'EASY BOSA (1002)' store_desc, 4 line_fct, 1002 id_fct, 2 line_jano, 10 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 13 (3811)' store_desc, 4 line_fct, 3811 id_fct, 2 line_jano, 811 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 170 (3014)' store_desc, 4 line_fct, 3014 id_fct, 2 line_jano, 14 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 80 (1004)' store_desc, 4 line_fct, 1004 id_fct, 2 line_jano, 11 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CENTRO MAYOR (3805)' store_desc, 4 line_fct, 3805 id_fct, 2 line_jano, 805 id_jano FROM DUAL UNION ALL
    SELECT 'EASY GAITAN CORTES (3813)' store_desc, 4 line_fct, 3813 id_fct, 2 line_jano, 813 id_jano FROM DUAL UNION ALL
    SELECT 'EASY HAYUELOS (12)' store_desc, 4 line_fct, 12 id_fct, 2 line_jano, 15 id_jano FROM DUAL UNION ALL
    SELECT 'EASY MAYALES VALLEDUPAR (3809)' store_desc, 4 line_fct, 3809 id_fct, 2 line_jano, 809 id_jano FROM DUAL UNION ALL
    SELECT 'EASY NORTE (3801)' store_desc, 4 line_fct, 3801 id_fct, 2 line_jano, 801 id_jano FROM DUAL UNION ALL
    SELECT 'EASY OCCIDENTE (3800)' store_desc, 4 line_fct, 3800 id_fct, 2 line_jano, 800 id_jano FROM DUAL UNION ALL
    SELECT 'EASY PRADO MEDELLIN (3806)' store_desc, 4 line_fct, 3806 id_fct, 2 line_jano, 806 id_jano FROM DUAL UNION ALL
    SELECT 'EASY SOACHA (3812)' store_desc, 4 line_fct, 3812 id_fct, 2 line_jano, 812 id_jano FROM DUAL UNION ALL
    SELECT 'EDS 1 MAYO (8)' store_desc, 3 line_fct, 8 id_fct, 1 line_jano, 8 id_jano FROM DUAL UNION ALL
    SELECT 'EDS ALAMOS (139)' store_desc, 3 line_fct, 139 id_fct, 1 line_jano, 139 id_jano FROM DUAL UNION ALL
    SELECT 'EDS ALQUERIA (149)' store_desc, 3 line_fct, 149 id_fct, 1 line_jano, 149 id_jano FROM DUAL UNION ALL
    SELECT 'EDS APOLO AUTOSUR (21)' store_desc, 3 line_fct, 21 id_fct, 1 line_jano, 21 id_jano FROM DUAL UNION ALL
    SELECT 'EDS AV DEL RIO (98)' store_desc, 3 line_fct, 98 id_fct, 1 line_jano, 98 id_jano FROM DUAL UNION ALL
    SELECT 'EDS AVD CIUDAD CALI (145)' store_desc, 3 line_fct, 145 id_fct, 1 line_jano, 145 id_jano FROM DUAL UNION ALL
    SELECT 'EDS BAHIA CL 46 (136)' store_desc, 3 line_fct, 136 id_fct, 1 line_jano, 136 id_jano FROM DUAL UNION ALL
    SELECT 'EDS CALLE 190 (161)' store_desc, 3 line_fct, 161 id_fct, 1 line_jano, 161 id_jano FROM DUAL UNION ALL
    SELECT 'EDS COLOMBIA CALLE 50 (7)' store_desc, 3 line_fct, 7 id_fct, 1 line_jano, 7 id_jano FROM DUAL UNION ALL
    SELECT 'EDS IVESUR CIRCUN (123)' store_desc, 3 line_fct, 123 id_fct, 1 line_jano, 123 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 17 CRA 17 (159)' store_desc, 3 line_fct, 159 id_fct, 1 line_jano, 159 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 24 CL 5B (132)' store_desc, 3 line_fct, 132 id_fct, 1 line_jano, 132 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 42 CL 34B (158)' store_desc, 3 line_fct, 158 id_fct, 1 line_jano, 158 id_jano FROM DUAL UNION ALL
    SELECT 'EDS MARRUECOS (2)' store_desc, 3 line_fct, 2 id_fct, 1 line_jano, 2 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SAN GABRIEL AERO (133)' store_desc, 3 line_fct, 133 id_fct, 1 line_jano, 133 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SEVILLANA (146)' store_desc, 3 line_fct, 146 id_fct, 1 line_jano, 146 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SIMON BOLIVAR CL 25 (134)' store_desc, 3 line_fct, 134 id_fct, 1 line_jano, 134 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SOACHA TERRENOS (160)' store_desc, 3 line_fct, 160 id_fct, 1 line_jano, 160 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TERCERA CL 34 (125)' store_desc, 3 line_fct, 125 id_fct, 1 line_jano, 125 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TINTALITO (101)' store_desc, 3 line_fct, 101 id_fct, 1 line_jano, 101 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TREBOL CL 76 (121)' store_desc, 3 line_fct, 121 id_fct, 1 line_jano, 121 id_jano FROM DUAL UNION ALL
    SELECT 'EDS YUMBO CRA 33 (102)' store_desc, 3 line_fct, 102 id_fct, 1 line_jano, 102 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO 20 DE JULIO (17)' store_desc, 2 line_fct, 17 id_fct, 1 line_jano, 17 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ALTOS DEL COUNTRY (249)' store_desc, 1 line_fct, 249 id_fct, 1 line_jano, 249 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ALTOS DEL PRADO (43)' store_desc, 1 line_fct, 43 id_fct, 1 line_jano, 43 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO AMERICANO (86)' store_desc, 1 line_fct, 86 id_fct, 1 line_jano, 86 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ATLANTIS (194)' store_desc, 1 line_fct, 194 id_fct, 1 line_jano, 194 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ATRIO (253)' store_desc, 1 line_fct, 253 id_fct, 1 line_jano, 253 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO AUTOPISTA SUR (18)' store_desc, 1 line_fct, 18 id_fct, 1 line_jano, 18 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO BUENAVISTA (88)' store_desc, 1 line_fct, 88 id_fct, 1 line_jano, 88 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO BULEVAR NIZA (3)' store_desc, 1 line_fct, 3 id_fct, 1 line_jano, 3 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CABECERA (103)' store_desc, 1 line_fct, 103 id_fct, 1 line_jano, 103 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CALLE 170 (14)' store_desc, 1 line_fct, 14 id_fct, 1 line_jano, 14 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CALLE 80 (11)' store_desc, 1 line_fct, 11 id_fct, 1 line_jano, 11 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CANAVERALL (108)' store_desc, 1 line_fct, 108 id_fct, 1 line_jano, 108 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CARIBE PLAZA (83)' store_desc, 1 line_fct, 83 id_fct, 1 line_jano, 83 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CARRERA 30 (16)' store_desc, 1 line_fct, 16 id_fct, 1 line_jano, 16 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIA (44)' store_desc, 1 line_fct, 44 id_fct, 1 line_jano, 44 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIA BAZAR (191)' store_desc, 1 line_fct, 191 id_fct, 1 line_jano, 191 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIPICHAPE (31)' store_desc, 1 line_fct, 31 id_fct, 1 line_jano, 31 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO DE LA 65 (23)' store_desc, 1 line_fct, 23 id_fct, 1 line_jano, 23 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO EL CASTILLO (174)' store_desc, 1 line_fct, 174 id_fct, 1 line_jano, 174 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO GIRARDOT (47)' store_desc, 1 line_fct, 47 id_fct, 1 line_jano, 47 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO GUATAPURI (87)' store_desc, 1 line_fct, 87 id_fct, 1 line_jano, 87 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO HAYUELOS (15)' store_desc, 1 line_fct, 15 id_fct, 1 line_jano, 15 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO LAS VEGAS (22)' store_desc, 1 line_fct, 22 id_fct, 1 line_jano, 22 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO LIMONAR PREMIER (30)' store_desc, 1 line_fct, 30 id_fct, 1 line_jano, 30 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO MEGA MALL (84)' store_desc, 1 line_fct, 84 id_fct, 1 line_jano, 84 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PASTO (128)' store_desc, 2 line_fct, 128 id_fct, 1 line_jano, 128 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PLAZA CENTRAL (193)' store_desc, 1 line_fct, 193 id_fct, 1 line_jano, 193 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO POPAYAN (36)' store_desc, 1 line_fct, 36 id_fct, 1 line_jano, 36 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PREMIUM PLAZA (24)' store_desc, 1 line_fct, 24 id_fct, 1 line_jano, 24 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO RIONEGRO (27)' store_desc, 1 line_fct, 27 id_fct, 1 line_jano, 27 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SAN SILVESTRE (126)' store_desc, 1 line_fct, 126 id_fct, 1 line_jano, 126 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA ANA (19)' store_desc, 1 line_fct, 19 id_fct, 1 line_jano, 19 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA FE (72)' store_desc, 1 line_fct, 72 id_fct, 1 line_jano, 72 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA MARTA (45)' store_desc, 1 line_fct, 45 id_fct, 1 line_jano, 45 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTAFE (148)' store_desc, 1 line_fct, 148 id_fct, 1 line_jano, 148 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SOACHA (48)' store_desc, 2 line_fct, 48 id_fct, 1 line_jano, 48 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SUBA (70)' store_desc, 1 line_fct, 70 id_fct, 1 line_jano, 70 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO TITAN (167)' store_desc, 1 line_fct, 167 id_fct, 1 line_jano, 167 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO TUNJA (76)' store_desc, 1 line_fct, 76 id_fct, 1 line_jano, 76 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO UNICENTRO (9)' store_desc, 1 line_fct, 9 id_fct, 1 line_jano, 9 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO VALLE DE LILI (13)' store_desc, 1 line_fct, 13 id_fct, 1 line_jano, 13 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO YOPAL (185)' store_desc, 1 line_fct, 185 id_fct, 1 line_jano, 185 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FATELARES (806)' store_desc, 2 line_fct, 806 id_fct, 1 line_jano, 806 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FONTIBON (78)' store_desc, 2 line_fct, 78 id_fct, 1 line_jano, 78 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MAYALES (184)' store_desc, 2 line_fct, 184 id_fct, 1 line_jano, 184 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ALQUERIA (124)' store_desc, 2 line_fct, 124 id_fct, 1 line_jano, 124 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ATALAYAS (82)' store_desc, 2 line_fct, 82 id_fct, 1 line_jano, 82 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BANDERAS (26)' store_desc, 2 line_fct, 26 id_fct, 1 line_jano, 26 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BELLO ANTIOQUIA (25)' store_desc, 2 line_fct, 25 id_fct, 1 line_jano, 25 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BOSA (10)' store_desc, 2 line_fct, 10 id_fct, 1 line_jano, 10 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BUGA (35)' store_desc, 2 line_fct, 35 id_fct, 1 line_jano, 35 id_jano FROM DUAL UNION ALL
    SELECT 'METRO CARTAGO (33)' store_desc, 2 line_fct, 33 id_fct, 1 line_jano, 33 id_jano FROM DUAL UNION ALL
    SELECT 'METRO DOSQUEBRADAS (166)' store_desc, 2 line_fct, 166 id_fct, 1 line_jano, 166 id_jano FROM DUAL UNION ALL
    SELECT 'METRO DUITAMA (28)' store_desc, 2 line_fct, 28 id_fct, 1 line_jano, 28 id_jano FROM DUAL UNION ALL
    SELECT 'METRO E_COMMERCE (203)' store_desc, 3 line_fct, 203 id_fct, 1 line_jano, 203 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS ALHAMBRA (334)' store_desc, 2 line_fct, 334 id_fct, 1 line_jano, 334 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS ANT COUNTRY (305)' store_desc, 2 line_fct, 305 id_fct, 1 line_jano, 305 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 125 (340)' store_desc, 2 line_fct, 340 id_fct, 1 line_jano, 340 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 148 (329)' store_desc, 2 line_fct, 329 id_fct, 1 line_jano, 329 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 45 (309)' store_desc, 2 line_fct, 309 id_fct, 1 line_jano, 309 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 93 (324)' store_desc, 2 line_fct, 324 id_fct, 1 line_jano, 324 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 95 (303)' store_desc, 2 line_fct, 303 id_fct, 1 line_jano, 303 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CARACAS CON 49 (304)' store_desc, 2 line_fct, 304 id_fct, 1 line_jano, 304 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CARRERA 3 (336)' store_desc, 2 line_fct, 336 id_fct, 1 line_jano, 336 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CEDRITOS CALL (301)' store_desc, 2 line_fct, 301 id_fct, 1 line_jano, 301 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CIUDAD SALITRE (337)' store_desc, 2 line_fct, 337 id_fct, 1 line_jano, 337 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CORFERIAS (333)' store_desc, 2 line_fct, 333 id_fct, 1 line_jano, 333 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS JAVERIANA 45 (335)' store_desc, 2 line_fct, 335 id_fct, 1 line_jano, 335 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FACATATIVA (74)' store_desc, 2 line_fct, 74 id_fct, 1 line_jano, 74 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FLORIDABLANCA (34)' store_desc, 2 line_fct, 34 id_fct, 1 line_jano, 34 id_jano FROM DUAL UNION ALL
    SELECT 'METRO GIRON (39)' store_desc, 2 line_fct, 39 id_fct, 1 line_jano, 39 id_jano FROM DUAL UNION ALL
    SELECT 'METRO IBAGUE (42)' store_desc, 2 line_fct, 42 id_fct, 1 line_jano, 42 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ITAGUI (46)' store_desc, 2 line_fct, 46 id_fct, 1 line_jano, 46 id_jano FROM DUAL UNION ALL
    SELECT 'METRO LA 70 (32)' store_desc, 2 line_fct, 32 id_fct, 1 line_jano, 32 id_jano FROM DUAL UNION ALL
    SELECT 'METRO LIBERTADORES (80)' store_desc, 2 line_fct, 80 id_fct, 1 line_jano, 80 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MONTERIA (85)' store_desc, 2 line_fct, 85 id_fct, 1 line_jano, 85 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MOSQUERA (73)' store_desc, 2 line_fct, 73 id_fct, 1 line_jano, 73 id_jano FROM DUAL UNION ALL
    SELECT 'METRO NEIVA (38)' store_desc, 2 line_fct, 38 id_fct, 1 line_jano, 38 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PALMIRA (6)' store_desc, 2 line_fct, 6 id_fct, 1 line_jano, 6 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PASTO UNICO (171)' store_desc, 2 line_fct, 171 id_fct, 1 line_jano, 171 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PITALITO (179)' store_desc, 2 line_fct, 179 id_fct, 1 line_jano, 179 id_jano FROM DUAL UNION ALL
    SELECT 'METRO RIOHACHA (40)' store_desc, 2 line_fct, 40 id_fct, 1 line_jano, 40 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SAN CAYETANO (79)' store_desc, 2 line_fct, 79 id_fct, 1 line_jano, 79 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SAN GIL (183)' store_desc, 2 line_fct, 183 id_fct, 1 line_jano, 183 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SANTA LUCIA (195)' store_desc, 2 line_fct, 195 id_fct, 1 line_jano, 195 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SIMON BOLIVAR (75)' store_desc, 2 line_fct, 75 id_fct, 1 line_jano, 75 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SOGAMOSO (97)' store_desc, 2 line_fct, 97 id_fct, 1 line_jano, 97 id_jano FROM DUAL UNION ALL
    SELECT 'METRO TINTALITO (71)' store_desc, 2 line_fct, 71 id_fct, 1 line_jano, 71 id_jano FROM DUAL UNION ALL
    SELECT 'METRO VENTURA (81)' store_desc, 2 line_fct, 81 id_fct, 1 line_jano, 81 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ZIPAQUIRA (77)' store_desc, 2 line_fct, 77 id_fct, 1 line_jano, 77 id_jano FROM DUAL
)
SELECT
    TO_CHAR(tr.id_tra) id_tra,
    vp.tpo_fctra_vep tipo_tr,
    tr.estdo_tra estado,
    TRIM(vp.prfjo_fctra_vep) prefijo_jan,
    TRIM(vp.fctra_vep) consecutivo_jan,
    TRIM(vp.prfjo_fctra_vep) || TRIM(vp.fctra_vep) factura_jan,
    TO_CHAR(es.line_jano) line_jan,
    es.store_desc tienda_desc_jan,
    TO_CHAR(es.id_fct) tienda_jan,
    TO_CHAR(tr.pos_tra) caja_jan,
    TO_CHAR(tr.transccion_tra) trx_jan,
    TO_CHAR(tr.fcha_crre_fdc, 'YYYY-MM-DD') fecha_cierre,
    TO_CHAR(tr.fcha_incia_tra, 'YYYY-MM-DD') fecha_ini,
    TO_CHAR(tr.fcha_fnlza_tra, 'YYYY-MM-DD') fecha_fin,
    TO_CHAR(vp.vlor_pgdo_vep) valor_jan,
    vp.id_clie cliente_jan,
    vp.tpo_id_clie tipo_identificacion,
    tr.id_cnal_vnta canal
FROM
    equivalent_store es
        INNER JOIN jano.trnsccion tr ON (
        es.line_jano = tr.id_neg
            AND es.id_jano = tr.id_tie
        )
        INNER JOIN jano.vntas_pos vp ON (
        tr.id_tra = vp.id_tra
            AND tr.id_neg = vp.id_neg
        )
WHERE
    tr.fcha_crre_fdc BETWEEN TO_DATE('{start_date}', 'YYYY-MM-DD') AND TO_DATE('{end_date}', 'YYYY-MM-DD')
  AND es.id_fct IN ({stores}) -- NEW
  AND tr.estdo_tra IN ('A', 'E')
  AND tr.id_neg IN (1, 2)
UNION ALL
SELECT
    TO_CHAR(tr.id_tra) id_tra,
    tr.id_ttr tipo_tr,
    tr.estdo_tra estado,
    TRIM(dp.prfjo_fctra_ddp) prefijo_jan,
    TRIM(dp.fctra_ddp) consecutivo_jan,
    TRIM(dp.prfjo_fctra_ddp) || TRIM(dp.fctra_ddp) AS factura_jan,
    TO_CHAR(es.line_jano) line_jan,
    es.store_desc tienda_desc_jan,
    TO_CHAR(es.id_fct) tienda_jan,
    TO_CHAR(tr.pos_tra) caja_jan,
    TO_CHAR(tr.transccion_tra) trx_jan,
    TO_CHAR(tr.fcha_crre_fdc, 'YYYY-MM-DD') fecha_cierre,
    TO_CHAR(tr.fcha_incia_tra, 'YYYY-MM-DD') fecha_ini,
    TO_CHAR(tr.fcha_fnlza_tra, 'YYYY-MM-DD') fecha_fin,
    '-' || TO_CHAR(dp.vlor_entrgdo_dep) valor_jan,
    dp.id_clie cliente_jan,
    dp.tpo_id_clie tipo_identificacion,
    tr.id_cnal_vnta canal
FROM
    equivalent_store es
        INNER JOIN jano.trnsccion tr ON (
        es.line_jano = tr.id_neg
            AND es.id_jano = tr.id_tie
        )
        INNER JOIN jano.dvlcnes_pos dp ON (
        tr.id_tra = dp.id_tra
            AND tr.id_neg = dp.id_neg
        )
WHERE
    tr.fcha_crre_fdc BETWEEN TO_DATE('{start_date}', 'YYYY-MM-DD') AND TO_DATE('{end_date}', 'YYYY-MM-DD')
  AND es.id_fct IN ({stores}) -- NEW
  AND dp.tpo_fctra_ddp IN ('F', 'P')
  AND tr.id_neg IN (1, 2)
  AND dp.prfjo_fctra_ddp NOT IN ('VCPM ')
"""


PAIR_EDOC_FCT_SQL = """WITH equivalent_store AS (
    SELECT 'CABECERA (322)' store_desc, 2 line_fct, 322 id_fct, 1 line_jano, 322 id_jano UNION ALL
    SELECT 'E_COMMERCE (204)' store_desc, 3 line_fct, 204 id_fct, 1 line_jano, 204 id_jano UNION ALL
    SELECT 'EASY 4SUR MEDELLIN (3814)' store_desc, 4 line_fct, 3814 id_fct, 2 line_jano, 814 id_jano UNION ALL
    SELECT 'EASY ALTOS DEL PRADO (3043)' store_desc, 4 line_fct, 3043 id_fct, 2 line_jano, 43 id_jano UNION ALL
    SELECT 'EASY AMERICAS (5)' store_desc, 4 line_fct, 5 id_fct, 2 line_jano, 802 id_jano UNION ALL
    SELECT 'EASY AUTOSUR (1006)' store_desc, 4 line_fct, 1006 id_fct, 2 line_jano, 18 id_jano UNION ALL
    SELECT 'EASY BOSA (1002)' store_desc, 4 line_fct, 1002 id_fct, 2 line_jano, 10 id_jano UNION ALL
    SELECT 'EASY CALLE 13 (3811)' store_desc, 4 line_fct, 3811 id_fct, 2 line_jano, 811 id_jano UNION ALL
    SELECT 'EASY CALLE 170 (3014)' store_desc, 4 line_fct, 3014 id_fct, 2 line_jano, 14 id_jano UNION ALL
    SELECT 'EASY CALLE 80 (1004)' store_desc, 4 line_fct, 1004 id_fct, 2 line_jano, 11 id_jano UNION ALL
    SELECT 'EASY CENTRO MAYOR (3805)' store_desc, 4 line_fct, 3805 id_fct, 2 line_jano, 805 id_jano UNION ALL
    SELECT 'EASY GAITAN CORTES (3813)' store_desc, 4 line_fct, 3813 id_fct, 2 line_jano, 813 id_jano UNION ALL
    SELECT 'EASY HAYUELOS (12)' store_desc, 4 line_fct, 12 id_fct, 2 line_jano, 15 id_jano UNION ALL
    SELECT 'EASY MAYALES VALLEDUPAR (3809)' store_desc, 4 line_fct, 3809 id_fct, 2 line_jano, 809 id_jano UNION ALL
    SELECT 'EASY NORTE (3801)' store_desc, 4 line_fct, 3801 id_fct, 2 line_jano, 801 id_jano UNION ALL
    SELECT 'EASY OCCIDENTE (3800)' store_desc, 4 line_fct, 3800 id_fct, 2 line_jano, 800 id_jano UNION ALL
    SELECT 'EASY PRADO MEDELLIN (3806)' store_desc, 4 line_fct, 3806 id_fct, 2 line_jano, 806 id_jano UNION ALL
    SELECT 'EASY SOACHA (3812)' store_desc, 4 line_fct, 3812 id_fct, 2 line_jano, 812 id_jano UNION ALL
    SELECT 'EDS 1 MAYO (8)' store_desc, 3 line_fct, 8 id_fct, 1 line_jano, 8 id_jano UNION ALL
    SELECT 'EDS ALAMOS (139)' store_desc, 3 line_fct, 139 id_fct, 1 line_jano, 139 id_jano UNION ALL
    SELECT 'EDS ALQUERIA (149)' store_desc, 3 line_fct, 149 id_fct, 1 line_jano, 149 id_jano UNION ALL
    SELECT 'EDS APOLO AUTOSUR (21)' store_desc, 3 line_fct, 21 id_fct, 1 line_jano, 21 id_jano UNION ALL
    SELECT 'EDS AV DEL RIO (98)' store_desc, 3 line_fct, 98 id_fct, 1 line_jano, 98 id_jano UNION ALL
    SELECT 'EDS AVD CIUDAD CALI (145)' store_desc, 3 line_fct, 145 id_fct, 1 line_jano, 145 id_jano UNION ALL
    SELECT 'EDS BAHIA CL 46 (136)' store_desc, 3 line_fct, 136 id_fct, 1 line_jano, 136 id_jano UNION ALL
    SELECT 'EDS CALLE 190 (161)' store_desc, 3 line_fct, 161 id_fct, 1 line_jano, 161 id_jano UNION ALL
    SELECT 'EDS COLOMBIA CALLE 50 (7)' store_desc, 3 line_fct, 7 id_fct, 1 line_jano, 7 id_jano UNION ALL
    SELECT 'EDS IVESUR CIRCUN (123)' store_desc, 3 line_fct, 123 id_fct, 1 line_jano, 123 id_jano UNION ALL
    SELECT 'EDS LA 17 CRA 17 (159)' store_desc, 3 line_fct, 159 id_fct, 1 line_jano, 159 id_jano UNION ALL
    SELECT 'EDS LA 24 CL 5B (132)' store_desc, 3 line_fct, 132 id_fct, 1 line_jano, 132 id_jano UNION ALL
    SELECT 'EDS LA 42 CL 34B (158)' store_desc, 3 line_fct, 158 id_fct, 1 line_jano, 158 id_jano UNION ALL
    SELECT 'EDS MARRUECOS (2)' store_desc, 3 line_fct, 2 id_fct, 1 line_jano, 2 id_jano UNION ALL
    SELECT 'EDS SAN GABRIEL AERO (133)' store_desc, 3 line_fct, 133 id_fct, 1 line_jano, 133 id_jano UNION ALL
    SELECT 'EDS SEVILLANA (146)' store_desc, 3 line_fct, 146 id_fct, 1 line_jano, 146 id_jano UNION ALL
    SELECT 'EDS SIMON BOLIVAR CL 25 (134)' store_desc, 3 line_fct, 134 id_fct, 1 line_jano, 134 id_jano UNION ALL
    SELECT 'EDS SOACHA TERRENOS (160)' store_desc, 3 line_fct, 160 id_fct, 1 line_jano, 160 id_jano UNION ALL
    SELECT 'EDS TERCERA CL 34 (125)' store_desc, 3 line_fct, 125 id_fct, 1 line_jano, 125 id_jano UNION ALL
    SELECT 'EDS TINTALITO (101)' store_desc, 3 line_fct, 101 id_fct, 1 line_jano, 101 id_jano UNION ALL
    SELECT 'EDS TREBOL CL 76 (121)' store_desc, 3 line_fct, 121 id_fct, 1 line_jano, 121 id_jano UNION ALL
    SELECT 'EDS YUMBO CRA 33 (102)' store_desc, 3 line_fct, 102 id_fct, 1 line_jano, 102 id_jano UNION ALL
    SELECT 'JUMBO 20 DE JULIO (17)' store_desc, 2 line_fct, 17 id_fct, 1 line_jano, 17 id_jano UNION ALL
    SELECT 'JUMBO ALTOS DEL COUNTRY (249)' store_desc, 1 line_fct, 249 id_fct, 1 line_jano, 249 id_jano UNION ALL
    SELECT 'JUMBO ALTOS DEL PRADO (43)' store_desc, 1 line_fct, 43 id_fct, 1 line_jano, 43 id_jano UNION ALL
    SELECT 'JUMBO AMERICANO (86)' store_desc, 1 line_fct, 86 id_fct, 1 line_jano, 86 id_jano UNION ALL
    SELECT 'JUMBO ATLANTIS (194)' store_desc, 1 line_fct, 194 id_fct, 1 line_jano, 194 id_jano UNION ALL
    SELECT 'JUMBO ATRIO (253)' store_desc, 1 line_fct, 253 id_fct, 1 line_jano, 253 id_jano UNION ALL
    SELECT 'JUMBO AUTOPISTA SUR (18)' store_desc, 1 line_fct, 18 id_fct, 1 line_jano, 18 id_jano UNION ALL
    SELECT 'JUMBO BUENAVISTA (88)' store_desc, 1 line_fct, 88 id_fct, 1 line_jano, 88 id_jano UNION ALL
    SELECT 'JUMBO BULEVAR NIZA (3)' store_desc, 1 line_fct, 3 id_fct, 1 line_jano, 3 id_jano UNION ALL
    SELECT 'JUMBO CABECERA (103)' store_desc, 1 line_fct, 103 id_fct, 1 line_jano, 103 id_jano UNION ALL
    SELECT 'JUMBO CALLE 170 (14)' store_desc, 1 line_fct, 14 id_fct, 1 line_jano, 14 id_jano UNION ALL
    SELECT 'JUMBO CALLE 80 (11)' store_desc, 1 line_fct, 11 id_fct, 1 line_jano, 11 id_jano UNION ALL
    SELECT 'JUMBO CANAVERALL (108)' store_desc, 1 line_fct, 108 id_fct, 1 line_jano, 108 id_jano UNION ALL
    SELECT 'JUMBO CARIBE PLAZA (83)' store_desc, 1 line_fct, 83 id_fct, 1 line_jano, 83 id_jano UNION ALL
    SELECT 'JUMBO CARRERA 30 (16)' store_desc, 1 line_fct, 16 id_fct, 1 line_jano, 16 id_jano UNION ALL
    SELECT 'JUMBO CHIA (44)' store_desc, 1 line_fct, 44 id_fct, 1 line_jano, 44 id_jano UNION ALL
    SELECT 'JUMBO CHIA BAZAR (191)' store_desc, 1 line_fct, 191 id_fct, 1 line_jano, 191 id_jano UNION ALL
    SELECT 'JUMBO CHIPICHAPE (31)' store_desc, 1 line_fct, 31 id_fct, 1 line_jano, 31 id_jano UNION ALL
    SELECT 'JUMBO DE LA 65 (23)' store_desc, 1 line_fct, 23 id_fct, 1 line_jano, 23 id_jano UNION ALL
    SELECT 'JUMBO EL CASTILLO (174)' store_desc, 1 line_fct, 174 id_fct, 1 line_jano, 174 id_jano UNION ALL
    SELECT 'JUMBO GIRARDOT (47)' store_desc, 1 line_fct, 47 id_fct, 1 line_jano, 47 id_jano UNION ALL
    SELECT 'JUMBO GUATAPURI (87)' store_desc, 1 line_fct, 87 id_fct, 1 line_jano, 87 id_jano UNION ALL
    SELECT 'JUMBO HAYUELOS (15)' store_desc, 1 line_fct, 15 id_fct, 1 line_jano, 15 id_jano UNION ALL
    SELECT 'JUMBO LAS VEGAS (22)' store_desc, 1 line_fct, 22 id_fct, 1 line_jano, 22 id_jano UNION ALL
    SELECT 'JUMBO LIMONAR PREMIER (30)' store_desc, 1 line_fct, 30 id_fct, 1 line_jano, 30 id_jano UNION ALL
    SELECT 'JUMBO MEGA MALL (84)' store_desc, 1 line_fct, 84 id_fct, 1 line_jano, 84 id_jano UNION ALL
    SELECT 'JUMBO PASTO (128)' store_desc, 2 line_fct, 128 id_fct, 1 line_jano, 128 id_jano UNION ALL
    SELECT 'JUMBO PLAZA CENTRAL (193)' store_desc, 1 line_fct, 193 id_fct, 1 line_jano, 193 id_jano UNION ALL
    SELECT 'JUMBO POPAYAN (36)' store_desc, 1 line_fct, 36 id_fct, 1 line_jano, 36 id_jano UNION ALL
    SELECT 'JUMBO PREMIUM PLAZA (24)' store_desc, 1 line_fct, 24 id_fct, 1 line_jano, 24 id_jano UNION ALL
    SELECT 'JUMBO RIONEGRO (27)' store_desc, 1 line_fct, 27 id_fct, 1 line_jano, 27 id_jano UNION ALL
    SELECT 'JUMBO SAN SILVESTRE (126)' store_desc, 1 line_fct, 126 id_fct, 1 line_jano, 126 id_jano UNION ALL
    SELECT 'JUMBO SANTA ANA (19)' store_desc, 1 line_fct, 19 id_fct, 1 line_jano, 19 id_jano UNION ALL
    SELECT 'JUMBO SANTA FE (72)' store_desc, 1 line_fct, 72 id_fct, 1 line_jano, 72 id_jano UNION ALL
    SELECT 'JUMBO SANTA MARTA (45)' store_desc, 1 line_fct, 45 id_fct, 1 line_jano, 45 id_jano UNION ALL
    SELECT 'JUMBO SANTAFE (148)' store_desc, 1 line_fct, 148 id_fct, 1 line_jano, 148 id_jano UNION ALL
    SELECT 'JUMBO SOACHA (48)' store_desc, 2 line_fct, 48 id_fct, 1 line_jano, 48 id_jano UNION ALL
    SELECT 'JUMBO SUBA (70)' store_desc, 1 line_fct, 70 id_fct, 1 line_jano, 70 id_jano UNION ALL
    SELECT 'JUMBO TITAN (167)' store_desc, 1 line_fct, 167 id_fct, 1 line_jano, 167 id_jano UNION ALL
    SELECT 'JUMBO TUNJA (76)' store_desc, 1 line_fct, 76 id_fct, 1 line_jano, 76 id_jano UNION ALL
    SELECT 'JUMBO UNICENTRO (9)' store_desc, 1 line_fct, 9 id_fct, 1 line_jano, 9 id_jano UNION ALL
    SELECT 'JUMBO VALLE DE LILI (13)' store_desc, 1 line_fct, 13 id_fct, 1 line_jano, 13 id_jano UNION ALL
    SELECT 'JUMBO YOPAL (185)' store_desc, 1 line_fct, 185 id_fct, 1 line_jano, 185 id_jano UNION ALL
    SELECT 'METRO FATELARES (806)' store_desc, 2 line_fct, 806 id_fct, 1 line_jano, 806 id_jano UNION ALL
    SELECT 'METRO FONTIBON (78)' store_desc, 2 line_fct, 78 id_fct, 1 line_jano, 78 id_jano UNION ALL
    SELECT 'METRO MAYALES (184)' store_desc, 2 line_fct, 184 id_fct, 1 line_jano, 184 id_jano UNION ALL
    SELECT 'METRO ALQUERIA (124)' store_desc, 2 line_fct, 124 id_fct, 1 line_jano, 124 id_jano UNION ALL
    SELECT 'METRO ATALAYAS (82)' store_desc, 2 line_fct, 82 id_fct, 1 line_jano, 82 id_jano UNION ALL
    SELECT 'METRO BANDERAS (26)' store_desc, 2 line_fct, 26 id_fct, 1 line_jano, 26 id_jano UNION ALL
    SELECT 'METRO BELLO ANTIOQUIA (25)' store_desc, 2 line_fct, 25 id_fct, 1 line_jano, 25 id_jano UNION ALL
    SELECT 'METRO BOSA (10)' store_desc, 2 line_fct, 10 id_fct, 1 line_jano, 10 id_jano UNION ALL
    SELECT 'METRO BUGA (35)' store_desc, 2 line_fct, 35 id_fct, 1 line_jano, 35 id_jano UNION ALL
    SELECT 'METRO CARTAGO (33)' store_desc, 2 line_fct, 33 id_fct, 1 line_jano, 33 id_jano UNION ALL
    SELECT 'METRO DOSQUEBRADAS (166)' store_desc, 2 line_fct, 166 id_fct, 1 line_jano, 166 id_jano UNION ALL
    SELECT 'METRO DUITAMA (28)' store_desc, 2 line_fct, 28 id_fct, 1 line_jano, 28 id_jano UNION ALL
    SELECT 'METRO E_COMMERCE (203)' store_desc, 3 line_fct, 203 id_fct, 1 line_jano, 203 id_jano UNION ALL
    SELECT 'METRO EXPRESS ALHAMBRA (334)' store_desc, 2 line_fct, 334 id_fct, 1 line_jano, 334 id_jano UNION ALL
    SELECT 'METRO EXPRESS ANT COUNTRY (305)' store_desc, 2 line_fct, 305 id_fct, 1 line_jano, 305 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 125 (340)' store_desc, 2 line_fct, 340 id_fct, 1 line_jano, 340 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 148 (329)' store_desc, 2 line_fct, 329 id_fct, 1 line_jano, 329 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 45 (309)' store_desc, 2 line_fct, 309 id_fct, 1 line_jano, 309 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 93 (324)' store_desc, 2 line_fct, 324 id_fct, 1 line_jano, 324 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 95 (303)' store_desc, 2 line_fct, 303 id_fct, 1 line_jano, 303 id_jano UNION ALL
    SELECT 'METRO EXPRESS CARACAS CON 49 (304)' store_desc, 2 line_fct, 304 id_fct, 1 line_jano, 304 id_jano UNION ALL
    SELECT 'METRO EXPRESS CARRERA 3 (336)' store_desc, 2 line_fct, 336 id_fct, 1 line_jano, 336 id_jano UNION ALL
    SELECT 'METRO EXPRESS CEDRITOS  CALL (301)' store_desc, 2 line_fct, 301 id_fct, 1 line_jano, 301 id_jano UNION ALL
    SELECT 'METRO EXPRESS CIUDAD SALITRE (337)' store_desc, 2 line_fct, 337 id_fct, 1 line_jano, 337 id_jano UNION ALL
    SELECT 'METRO EXPRESS CORFERIAS (333)' store_desc, 2 line_fct, 333 id_fct, 1 line_jano, 333 id_jano UNION ALL
    SELECT 'METRO EXPRESS JAVERIANA 45 (335)' store_desc, 2 line_fct, 335 id_fct, 1 line_jano, 335 id_jano UNION ALL
    SELECT 'METRO FACATATIVA (74)' store_desc, 2 line_fct, 74 id_fct, 1 line_jano, 74 id_jano UNION ALL
    SELECT 'METRO FLORIDABLANCA (34)' store_desc, 2 line_fct, 34 id_fct, 1 line_jano, 34 id_jano UNION ALL
    SELECT 'METRO GIRON (39)' store_desc, 2 line_fct, 39 id_fct, 1 line_jano, 39 id_jano UNION ALL
    SELECT 'METRO IBAGUE (42)' store_desc, 2 line_fct, 42 id_fct, 1 line_jano, 42 id_jano UNION ALL
    SELECT 'METRO ITAGUI (46)' store_desc, 2 line_fct, 46 id_fct, 1 line_jano, 46 id_jano UNION ALL
    SELECT 'METRO LA 70 (32)' store_desc, 2 line_fct, 32 id_fct, 1 line_jano, 32 id_jano UNION ALL
    SELECT 'METRO LIBERTADORES (80)' store_desc, 2 line_fct, 80 id_fct, 1 line_jano, 80 id_jano UNION ALL
    SELECT 'METRO MONTERIA (85)' store_desc, 2 line_fct, 85 id_fct, 1 line_jano, 85 id_jano UNION ALL
    SELECT 'METRO MOSQUERA (73)' store_desc, 2 line_fct, 73 id_fct, 1 line_jano, 73 id_jano UNION ALL
    SELECT 'METRO NEIVA (38)' store_desc, 2 line_fct, 38 id_fct, 1 line_jano, 38 id_jano UNION ALL
    SELECT 'METRO PALMIRA (6)' store_desc, 2 line_fct, 6 id_fct, 1 line_jano, 6 id_jano UNION ALL
    SELECT 'METRO PASTO UNICO (171)' store_desc, 2 line_fct, 171 id_fct, 1 line_jano, 171 id_jano UNION ALL
    SELECT 'METRO PITALITO (179)' store_desc, 2 line_fct, 179 id_fct, 1 line_jano, 179 id_jano UNION ALL
    SELECT 'METRO RIOHACHA (40)' store_desc, 2 line_fct, 40 id_fct, 1 line_jano, 40 id_jano UNION ALL
    SELECT 'METRO SAN CAYETANO (79)' store_desc, 2 line_fct, 79 id_fct, 1 line_jano, 79 id_jano UNION ALL
    SELECT 'METRO SAN GIL (183)' store_desc, 2 line_fct, 183 id_fct, 1 line_jano, 183 id_jano UNION ALL
    SELECT 'METRO SANTA LUCIA (195)' store_desc, 2 line_fct, 195 id_fct, 1 line_jano, 195 id_jano UNION ALL
    SELECT 'METRO SIMON BOLIVAR (75)' store_desc, 2 line_fct, 75 id_fct, 1 line_jano, 75 id_jano UNION ALL
    SELECT 'METRO SOGAMOSO (97)' store_desc, 2 line_fct, 97 id_fct, 1 line_jano, 97 id_jano UNION ALL
    SELECT 'METRO TINTALITO (71)' store_desc, 2 line_fct, 71 id_fct, 1 line_jano, 71 id_jano UNION ALL
    SELECT 'METRO VENTURA (81)' store_desc, 2 line_fct, 81 id_fct, 1 line_jano, 81 id_jano UNION ALL
    SELECT 'METRO ZIPAQUIRA (77)' store_desc, 2 line_fct, 77 id_fct, 1 line_jano, 77 id_jano
)
SELECT DISTINCT
    ef.encfactura_col_id::VARCHAR id_fct,
    ef.c_origen::VARCHAR,
    SUBSTRING(ef.num_doc_fact_elec, 1, 4) prefijo_fct,
    SUBSTRING(ef.num_doc_fact_elec, 4) consecutivo_fct,
    ef.num_doc_fact_elec factura_fct,
    ef.nro_factura_afec,
    es.line_jano::VARCHAR line_fct,
    es.store_desc tienda_desc_fct,
    es.id_fct::VARCHAR tienda_fct,
    REGEXP_REPLACE(ef.nro_terminal, '^0+', '') caja_fct,
    ef.cod_prov::VARCHAR trx_fct,
    ef.fec_fact::DATE fecha_fct,
    EXTRACT(MONTH FROM efe.f_envio_dian) mes,
    CASE
        WHEN ef.c_origen IN (4, 9) THEN '-' || ef.vt_factura::INT8::VARCHAR
        ELSE ef.vt_factura::INT8::VARCHAR
    END valor_fct,
    ef.nit_prov::VARCHAR cliente_fct,
    ef.factura_duplicada duplicada,
    efe.f_envio_dian::DATE,
    efe.estado_dian,
    efe.log_errores_dian,
    efe.cufe
FROM
    factura.estado_fact_electronica efe
        INNER JOIN factura.encabezado_factura ef ON efe.encfactura_id = ef.encfactura_col_id
            AND efe.estado_dian = 'OK'
        INNER JOIN equivalent_store es ON ef.codigo_tienda = es.id_fct
WHERE
    ef.fec_fact::DATE BETWEEN '{start_date}' AND '{end_date}'
  AND ef.num_doc_fact_elec = '{edoc}'
  AND ef.cod_prov = {trx}"""


PAIR_SPTD_FCT_SQL = """WITH equivalent_store AS (
    SELECT 'CABECERA (322)' store_desc, 2 line_fct, 322 id_fct, 1 line_jano, 322 id_jano UNION ALL
    SELECT 'E_COMMERCE (204)' store_desc, 3 line_fct, 204 id_fct, 1 line_jano, 204 id_jano UNION ALL
    SELECT 'EASY 4SUR MEDELLIN (3814)' store_desc, 4 line_fct, 3814 id_fct, 2 line_jano, 814 id_jano UNION ALL
    SELECT 'EASY ALTOS DEL PRADO (3043)' store_desc, 4 line_fct, 3043 id_fct, 2 line_jano, 43 id_jano UNION ALL
    SELECT 'EASY AMERICAS (5)' store_desc, 4 line_fct, 5 id_fct, 2 line_jano, 802 id_jano UNION ALL
    SELECT 'EASY AUTOSUR (1006)' store_desc, 4 line_fct, 1006 id_fct, 2 line_jano, 18 id_jano UNION ALL
    SELECT 'EASY BOSA (1002)' store_desc, 4 line_fct, 1002 id_fct, 2 line_jano, 10 id_jano UNION ALL
    SELECT 'EASY CALLE 13 (3811)' store_desc, 4 line_fct, 3811 id_fct, 2 line_jano, 811 id_jano UNION ALL
    SELECT 'EASY CALLE 170 (3014)' store_desc, 4 line_fct, 3014 id_fct, 2 line_jano, 14 id_jano UNION ALL
    SELECT 'EASY CALLE 80 (1004)' store_desc, 4 line_fct, 1004 id_fct, 2 line_jano, 11 id_jano UNION ALL
    SELECT 'EASY CENTRO MAYOR (3805)' store_desc, 4 line_fct, 3805 id_fct, 2 line_jano, 805 id_jano UNION ALL
    SELECT 'EASY GAITAN CORTES (3813)' store_desc, 4 line_fct, 3813 id_fct, 2 line_jano, 813 id_jano UNION ALL
    SELECT 'EASY HAYUELOS (12)' store_desc, 4 line_fct, 12 id_fct, 2 line_jano, 15 id_jano UNION ALL
    SELECT 'EASY MAYALES VALLEDUPAR (3809)' store_desc, 4 line_fct, 3809 id_fct, 2 line_jano, 809 id_jano UNION ALL
    SELECT 'EASY NORTE (3801)' store_desc, 4 line_fct, 3801 id_fct, 2 line_jano, 801 id_jano UNION ALL
    SELECT 'EASY OCCIDENTE (3800)' store_desc, 4 line_fct, 3800 id_fct, 2 line_jano, 800 id_jano UNION ALL
    SELECT 'EASY PRADO MEDELLIN (3806)' store_desc, 4 line_fct, 3806 id_fct, 2 line_jano, 806 id_jano UNION ALL
    SELECT 'EASY SOACHA (3812)' store_desc, 4 line_fct, 3812 id_fct, 2 line_jano, 812 id_jano UNION ALL
    SELECT 'EDS 1 MAYO (8)' store_desc, 3 line_fct, 8 id_fct, 1 line_jano, 8 id_jano UNION ALL
    SELECT 'EDS ALAMOS (139)' store_desc, 3 line_fct, 139 id_fct, 1 line_jano, 139 id_jano UNION ALL
    SELECT 'EDS ALQUERIA (149)' store_desc, 3 line_fct, 149 id_fct, 1 line_jano, 149 id_jano UNION ALL
    SELECT 'EDS APOLO AUTOSUR (21)' store_desc, 3 line_fct, 21 id_fct, 1 line_jano, 21 id_jano UNION ALL
    SELECT 'EDS AV DEL RIO (98)' store_desc, 3 line_fct, 98 id_fct, 1 line_jano, 98 id_jano UNION ALL
    SELECT 'EDS AVD CIUDAD CALI (145)' store_desc, 3 line_fct, 145 id_fct, 1 line_jano, 145 id_jano UNION ALL
    SELECT 'EDS BAHIA CL 46 (136)' store_desc, 3 line_fct, 136 id_fct, 1 line_jano, 136 id_jano UNION ALL
    SELECT 'EDS CALLE 190 (161)' store_desc, 3 line_fct, 161 id_fct, 1 line_jano, 161 id_jano UNION ALL
    SELECT 'EDS COLOMBIA CALLE 50 (7)' store_desc, 3 line_fct, 7 id_fct, 1 line_jano, 7 id_jano UNION ALL
    SELECT 'EDS IVESUR CIRCUN (123)' store_desc, 3 line_fct, 123 id_fct, 1 line_jano, 123 id_jano UNION ALL
    SELECT 'EDS LA 17 CRA 17 (159)' store_desc, 3 line_fct, 159 id_fct, 1 line_jano, 159 id_jano UNION ALL
    SELECT 'EDS LA 24 CL 5B (132)' store_desc, 3 line_fct, 132 id_fct, 1 line_jano, 132 id_jano UNION ALL
    SELECT 'EDS LA 42 CL 34B (158)' store_desc, 3 line_fct, 158 id_fct, 1 line_jano, 158 id_jano UNION ALL
    SELECT 'EDS MARRUECOS (2)' store_desc, 3 line_fct, 2 id_fct, 1 line_jano, 2 id_jano UNION ALL
    SELECT 'EDS SAN GABRIEL AERO (133)' store_desc, 3 line_fct, 133 id_fct, 1 line_jano, 133 id_jano UNION ALL
    SELECT 'EDS SEVILLANA (146)' store_desc, 3 line_fct, 146 id_fct, 1 line_jano, 146 id_jano UNION ALL
    SELECT 'EDS SIMON BOLIVAR CL 25 (134)' store_desc, 3 line_fct, 134 id_fct, 1 line_jano, 134 id_jano UNION ALL
    SELECT 'EDS SOACHA TERRENOS (160)' store_desc, 3 line_fct, 160 id_fct, 1 line_jano, 160 id_jano UNION ALL
    SELECT 'EDS TERCERA CL 34 (125)' store_desc, 3 line_fct, 125 id_fct, 1 line_jano, 125 id_jano UNION ALL
    SELECT 'EDS TINTALITO (101)' store_desc, 3 line_fct, 101 id_fct, 1 line_jano, 101 id_jano UNION ALL
    SELECT 'EDS TREBOL CL 76 (121)' store_desc, 3 line_fct, 121 id_fct, 1 line_jano, 121 id_jano UNION ALL
    SELECT 'EDS YUMBO CRA 33 (102)' store_desc, 3 line_fct, 102 id_fct, 1 line_jano, 102 id_jano UNION ALL
    SELECT 'JUMBO 20 DE JULIO (17)' store_desc, 2 line_fct, 17 id_fct, 1 line_jano, 17 id_jano UNION ALL
    SELECT 'JUMBO ALTOS DEL COUNTRY (249)' store_desc, 1 line_fct, 249 id_fct, 1 line_jano, 249 id_jano UNION ALL
    SELECT 'JUMBO ALTOS DEL PRADO (43)' store_desc, 1 line_fct, 43 id_fct, 1 line_jano, 43 id_jano UNION ALL
    SELECT 'JUMBO AMERICANO (86)' store_desc, 1 line_fct, 86 id_fct, 1 line_jano, 86 id_jano UNION ALL
    SELECT 'JUMBO ATLANTIS (194)' store_desc, 1 line_fct, 194 id_fct, 1 line_jano, 194 id_jano UNION ALL
    SELECT 'JUMBO ATRIO (253)' store_desc, 1 line_fct, 253 id_fct, 1 line_jano, 253 id_jano UNION ALL
    SELECT 'JUMBO AUTOPISTA SUR (18)' store_desc, 1 line_fct, 18 id_fct, 1 line_jano, 18 id_jano UNION ALL
    SELECT 'JUMBO BUENAVISTA (88)' store_desc, 1 line_fct, 88 id_fct, 1 line_jano, 88 id_jano UNION ALL
    SELECT 'JUMBO BULEVAR NIZA (3)' store_desc, 1 line_fct, 3 id_fct, 1 line_jano, 3 id_jano UNION ALL
    SELECT 'JUMBO CABECERA (103)' store_desc, 1 line_fct, 103 id_fct, 1 line_jano, 103 id_jano UNION ALL
    SELECT 'JUMBO CALLE 170 (14)' store_desc, 1 line_fct, 14 id_fct, 1 line_jano, 14 id_jano UNION ALL
    SELECT 'JUMBO CALLE 80 (11)' store_desc, 1 line_fct, 11 id_fct, 1 line_jano, 11 id_jano UNION ALL
    SELECT 'JUMBO CANAVERALL (108)' store_desc, 1 line_fct, 108 id_fct, 1 line_jano, 108 id_jano UNION ALL
    SELECT 'JUMBO CARIBE PLAZA (83)' store_desc, 1 line_fct, 83 id_fct, 1 line_jano, 83 id_jano UNION ALL
    SELECT 'JUMBO CARRERA 30 (16)' store_desc, 1 line_fct, 16 id_fct, 1 line_jano, 16 id_jano UNION ALL
    SELECT 'JUMBO CHIA (44)' store_desc, 1 line_fct, 44 id_fct, 1 line_jano, 44 id_jano UNION ALL
    SELECT 'JUMBO CHIA BAZAR (191)' store_desc, 1 line_fct, 191 id_fct, 1 line_jano, 191 id_jano UNION ALL
    SELECT 'JUMBO CHIPICHAPE (31)' store_desc, 1 line_fct, 31 id_fct, 1 line_jano, 31 id_jano UNION ALL
    SELECT 'JUMBO DE LA 65 (23)' store_desc, 1 line_fct, 23 id_fct, 1 line_jano, 23 id_jano UNION ALL
    SELECT 'JUMBO EL CASTILLO (174)' store_desc, 1 line_fct, 174 id_fct, 1 line_jano, 174 id_jano UNION ALL
    SELECT 'JUMBO GIRARDOT (47)' store_desc, 1 line_fct, 47 id_fct, 1 line_jano, 47 id_jano UNION ALL
    SELECT 'JUMBO GUATAPURI (87)' store_desc, 1 line_fct, 87 id_fct, 1 line_jano, 87 id_jano UNION ALL
    SELECT 'JUMBO HAYUELOS (15)' store_desc, 1 line_fct, 15 id_fct, 1 line_jano, 15 id_jano UNION ALL
    SELECT 'JUMBO LAS VEGAS (22)' store_desc, 1 line_fct, 22 id_fct, 1 line_jano, 22 id_jano UNION ALL
    SELECT 'JUMBO LIMONAR PREMIER (30)' store_desc, 1 line_fct, 30 id_fct, 1 line_jano, 30 id_jano UNION ALL
    SELECT 'JUMBO MEGA MALL (84)' store_desc, 1 line_fct, 84 id_fct, 1 line_jano, 84 id_jano UNION ALL
    SELECT 'JUMBO PASTO (128)' store_desc, 2 line_fct, 128 id_fct, 1 line_jano, 128 id_jano UNION ALL
    SELECT 'JUMBO PLAZA CENTRAL (193)' store_desc, 1 line_fct, 193 id_fct, 1 line_jano, 193 id_jano UNION ALL
    SELECT 'JUMBO POPAYAN (36)' store_desc, 1 line_fct, 36 id_fct, 1 line_jano, 36 id_jano UNION ALL
    SELECT 'JUMBO PREMIUM PLAZA (24)' store_desc, 1 line_fct, 24 id_fct, 1 line_jano, 24 id_jano UNION ALL
    SELECT 'JUMBO RIONEGRO (27)' store_desc, 1 line_fct, 27 id_fct, 1 line_jano, 27 id_jano UNION ALL
    SELECT 'JUMBO SAN SILVESTRE (126)' store_desc, 1 line_fct, 126 id_fct, 1 line_jano, 126 id_jano UNION ALL
    SELECT 'JUMBO SANTA ANA (19)' store_desc, 1 line_fct, 19 id_fct, 1 line_jano, 19 id_jano UNION ALL
    SELECT 'JUMBO SANTA FE (72)' store_desc, 1 line_fct, 72 id_fct, 1 line_jano, 72 id_jano UNION ALL
    SELECT 'JUMBO SANTA MARTA (45)' store_desc, 1 line_fct, 45 id_fct, 1 line_jano, 45 id_jano UNION ALL
    SELECT 'JUMBO SANTAFE (148)' store_desc, 1 line_fct, 148 id_fct, 1 line_jano, 148 id_jano UNION ALL
    SELECT 'JUMBO SOACHA (48)' store_desc, 2 line_fct, 48 id_fct, 1 line_jano, 48 id_jano UNION ALL
    SELECT 'JUMBO SUBA (70)' store_desc, 1 line_fct, 70 id_fct, 1 line_jano, 70 id_jano UNION ALL
    SELECT 'JUMBO TITAN (167)' store_desc, 1 line_fct, 167 id_fct, 1 line_jano, 167 id_jano UNION ALL
    SELECT 'JUMBO TUNJA (76)' store_desc, 1 line_fct, 76 id_fct, 1 line_jano, 76 id_jano UNION ALL
    SELECT 'JUMBO UNICENTRO (9)' store_desc, 1 line_fct, 9 id_fct, 1 line_jano, 9 id_jano UNION ALL
    SELECT 'JUMBO VALLE DE LILI (13)' store_desc, 1 line_fct, 13 id_fct, 1 line_jano, 13 id_jano UNION ALL
    SELECT 'JUMBO YOPAL (185)' store_desc, 1 line_fct, 185 id_fct, 1 line_jano, 185 id_jano UNION ALL
    SELECT 'METRO FATELARES (806)' store_desc, 2 line_fct, 806 id_fct, 1 line_jano, 806 id_jano UNION ALL
    SELECT 'METRO FONTIBON (78)' store_desc, 2 line_fct, 78 id_fct, 1 line_jano, 78 id_jano UNION ALL
    SELECT 'METRO MAYALES (184)' store_desc, 2 line_fct, 184 id_fct, 1 line_jano, 184 id_jano UNION ALL
    SELECT 'METRO ALQUERIA (124)' store_desc, 2 line_fct, 124 id_fct, 1 line_jano, 124 id_jano UNION ALL
    SELECT 'METRO ATALAYAS (82)' store_desc, 2 line_fct, 82 id_fct, 1 line_jano, 82 id_jano UNION ALL
    SELECT 'METRO BANDERAS (26)' store_desc, 2 line_fct, 26 id_fct, 1 line_jano, 26 id_jano UNION ALL
    SELECT 'METRO BELLO ANTIOQUIA (25)' store_desc, 2 line_fct, 25 id_fct, 1 line_jano, 25 id_jano UNION ALL
    SELECT 'METRO BOSA (10)' store_desc, 2 line_fct, 10 id_fct, 1 line_jano, 10 id_jano UNION ALL
    SELECT 'METRO BUGA (35)' store_desc, 2 line_fct, 35 id_fct, 1 line_jano, 35 id_jano UNION ALL
    SELECT 'METRO CARTAGO (33)' store_desc, 2 line_fct, 33 id_fct, 1 line_jano, 33 id_jano UNION ALL
    SELECT 'METRO DOSQUEBRADAS (166)' store_desc, 2 line_fct, 166 id_fct, 1 line_jano, 166 id_jano UNION ALL
    SELECT 'METRO DUITAMA (28)' store_desc, 2 line_fct, 28 id_fct, 1 line_jano, 28 id_jano UNION ALL
    SELECT 'METRO E_COMMERCE (203)' store_desc, 3 line_fct, 203 id_fct, 1 line_jano, 203 id_jano UNION ALL
    SELECT 'METRO EXPRESS ALHAMBRA (334)' store_desc, 2 line_fct, 334 id_fct, 1 line_jano, 334 id_jano UNION ALL
    SELECT 'METRO EXPRESS ANT COUNTRY (305)' store_desc, 2 line_fct, 305 id_fct, 1 line_jano, 305 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 125 (340)' store_desc, 2 line_fct, 340 id_fct, 1 line_jano, 340 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 148 (329)' store_desc, 2 line_fct, 329 id_fct, 1 line_jano, 329 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 45 (309)' store_desc, 2 line_fct, 309 id_fct, 1 line_jano, 309 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 93 (324)' store_desc, 2 line_fct, 324 id_fct, 1 line_jano, 324 id_jano UNION ALL
    SELECT 'METRO EXPRESS CALLE 95 (303)' store_desc, 2 line_fct, 303 id_fct, 1 line_jano, 303 id_jano UNION ALL
    SELECT 'METRO EXPRESS CARACAS CON 49 (304)' store_desc, 2 line_fct, 304 id_fct, 1 line_jano, 304 id_jano UNION ALL
    SELECT 'METRO EXPRESS CARRERA 3 (336)' store_desc, 2 line_fct, 336 id_fct, 1 line_jano, 336 id_jano UNION ALL
    SELECT 'METRO EXPRESS CEDRITOS  CALL (301)' store_desc, 2 line_fct, 301 id_fct, 1 line_jano, 301 id_jano UNION ALL
    SELECT 'METRO EXPRESS CIUDAD SALITRE (337)' store_desc, 2 line_fct, 337 id_fct, 1 line_jano, 337 id_jano UNION ALL
    SELECT 'METRO EXPRESS CORFERIAS (333)' store_desc, 2 line_fct, 333 id_fct, 1 line_jano, 333 id_jano UNION ALL
    SELECT 'METRO EXPRESS JAVERIANA 45 (335)' store_desc, 2 line_fct, 335 id_fct, 1 line_jano, 335 id_jano UNION ALL
    SELECT 'METRO FACATATIVA (74)' store_desc, 2 line_fct, 74 id_fct, 1 line_jano, 74 id_jano UNION ALL
    SELECT 'METRO FLORIDABLANCA (34)' store_desc, 2 line_fct, 34 id_fct, 1 line_jano, 34 id_jano UNION ALL
    SELECT 'METRO GIRON (39)' store_desc, 2 line_fct, 39 id_fct, 1 line_jano, 39 id_jano UNION ALL
    SELECT 'METRO IBAGUE (42)' store_desc, 2 line_fct, 42 id_fct, 1 line_jano, 42 id_jano UNION ALL
    SELECT 'METRO ITAGUI (46)' store_desc, 2 line_fct, 46 id_fct, 1 line_jano, 46 id_jano UNION ALL
    SELECT 'METRO LA 70 (32)' store_desc, 2 line_fct, 32 id_fct, 1 line_jano, 32 id_jano UNION ALL
    SELECT 'METRO LIBERTADORES (80)' store_desc, 2 line_fct, 80 id_fct, 1 line_jano, 80 id_jano UNION ALL
    SELECT 'METRO MONTERIA (85)' store_desc, 2 line_fct, 85 id_fct, 1 line_jano, 85 id_jano UNION ALL
    SELECT 'METRO MOSQUERA (73)' store_desc, 2 line_fct, 73 id_fct, 1 line_jano, 73 id_jano UNION ALL
    SELECT 'METRO NEIVA (38)' store_desc, 2 line_fct, 38 id_fct, 1 line_jano, 38 id_jano UNION ALL
    SELECT 'METRO PALMIRA (6)' store_desc, 2 line_fct, 6 id_fct, 1 line_jano, 6 id_jano UNION ALL
    SELECT 'METRO PASTO UNICO (171)' store_desc, 2 line_fct, 171 id_fct, 1 line_jano, 171 id_jano UNION ALL
    SELECT 'METRO PITALITO (179)' store_desc, 2 line_fct, 179 id_fct, 1 line_jano, 179 id_jano UNION ALL
    SELECT 'METRO RIOHACHA (40)' store_desc, 2 line_fct, 40 id_fct, 1 line_jano, 40 id_jano UNION ALL
    SELECT 'METRO SAN CAYETANO (79)' store_desc, 2 line_fct, 79 id_fct, 1 line_jano, 79 id_jano UNION ALL
    SELECT 'METRO SAN GIL (183)' store_desc, 2 line_fct, 183 id_fct, 1 line_jano, 183 id_jano UNION ALL
    SELECT 'METRO SANTA LUCIA (195)' store_desc, 2 line_fct, 195 id_fct, 1 line_jano, 195 id_jano UNION ALL
    SELECT 'METRO SIMON BOLIVAR (75)' store_desc, 2 line_fct, 75 id_fct, 1 line_jano, 75 id_jano UNION ALL
    SELECT 'METRO SOGAMOSO (97)' store_desc, 2 line_fct, 97 id_fct, 1 line_jano, 97 id_jano UNION ALL
    SELECT 'METRO TINTALITO (71)' store_desc, 2 line_fct, 71 id_fct, 1 line_jano, 71 id_jano UNION ALL
    SELECT 'METRO VENTURA (81)' store_desc, 2 line_fct, 81 id_fct, 1 line_jano, 81 id_jano UNION ALL
    SELECT 'METRO ZIPAQUIRA (77)' store_desc, 2 line_fct, 77 id_fct, 1 line_jano, 77 id_jano
)
SELECT DISTINCT
    ef.encfactura_col_id::VARCHAR id_fct,
    ef.c_origen::VARCHAR,
    SUBSTRING(ef.num_doc_fact_elec, 1, 4) prefijo_fct,
    SUBSTRING(ef.num_doc_fact_elec, 4) consecutivo_fct,
    ef.num_doc_fact_elec factura_fct,
    ef.nro_factura_afec,
    es.line_jano::VARCHAR line_fct,
    es.store_desc tienda_desc_fct,
    es.id_fct::VARCHAR tienda_fct,
    REGEXP_REPLACE(ef.nro_terminal, '^0+', '') caja_fct,
    ef.cod_prov::VARCHAR trx_fct,
    ef.fec_fact::DATE fecha_fct,
    EXTRACT(MONTH FROM efe.f_envio_dian) mes,
    CASE
        WHEN ef.c_origen IN (4, 9) THEN '-' || ef.vt_factura::INT8::VARCHAR
        ELSE ef.vt_factura::INT8::VARCHAR
    END valor_fct,
    ef.nit_prov::VARCHAR cliente_fct,
    ef.factura_duplicada duplicada,
    efe.f_envio_dian::DATE,
    efe.estado_dian,
    efe.log_errores_dian,
    efe.cufe
FROM
    factura.estado_fact_electronica efe
        INNER JOIN factura.encabezado_factura ef ON efe.encfactura_id = ef.encfactura_col_id
        AND efe.estado_dian = 'OK'
        INNER JOIN equivalent_store es ON ef.codigo_tienda = es.id_fct
WHERE
    ef.fec_fact::DATE BETWEEN '{start_date}' AND '{end_date}'
  AND es.id_fct = {store}
  AND LPAD(ef.nro_terminal, 2, '0') = '{pos}'
  AND ef.cod_prov = {trx}"""


PAIR_FT_JAN_SQL = """WITH equivalent_store AS (
    SELECT 'CABECERA (322)' store_desc, 2 line_fct, 322 id_fct, 1 line_jano, 322 id_jano FROM DUAL UNION ALL
    SELECT 'E_COMMERCE (204)' store_desc, 3 line_fct, 204 id_fct, 1 line_jano, 204 id_jano FROM DUAL UNION ALL
    SELECT 'EASY 4SUR MEDELLIN (3814)' store_desc, 4 line_fct, 3814 id_fct, 2 line_jano, 814 id_jano FROM DUAL UNION ALL
    SELECT 'EASY ALTOS DEL PRADO (3043)' store_desc, 4 line_fct, 3043 id_fct, 2 line_jano, 43 id_jano FROM DUAL UNION ALL
    SELECT 'EASY AMERICAS (5)' store_desc, 4 line_fct, 5 id_fct, 2 line_jano, 802 id_jano FROM DUAL UNION ALL
    SELECT 'EASY AUTOSUR (1006)' store_desc, 4 line_fct, 1006 id_fct, 2 line_jano, 18 id_jano FROM DUAL UNION ALL
    SELECT 'EASY BOSA (1002)' store_desc, 4 line_fct, 1002 id_fct, 2 line_jano, 10 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 13 (3811)' store_desc, 4 line_fct, 3811 id_fct, 2 line_jano, 811 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 170 (3014)' store_desc, 4 line_fct, 3014 id_fct, 2 line_jano, 14 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 80 (1004)' store_desc, 4 line_fct, 1004 id_fct, 2 line_jano, 11 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CENTRO MAYOR (3805)' store_desc, 4 line_fct, 3805 id_fct, 2 line_jano, 805 id_jano FROM DUAL UNION ALL
    SELECT 'EASY GAITAN CORTES (3813)' store_desc, 4 line_fct, 3813 id_fct, 2 line_jano, 813 id_jano FROM DUAL UNION ALL
    SELECT 'EASY HAYUELOS (12)' store_desc, 4 line_fct, 12 id_fct, 2 line_jano, 15 id_jano FROM DUAL UNION ALL
    SELECT 'EASY MAYALES VALLEDUPAR (3809)' store_desc, 4 line_fct, 3809 id_fct, 2 line_jano, 809 id_jano FROM DUAL UNION ALL
    SELECT 'EASY NORTE (3801)' store_desc, 4 line_fct, 3801 id_fct, 2 line_jano, 801 id_jano FROM DUAL UNION ALL
    SELECT 'EASY OCCIDENTE (3800)' store_desc, 4 line_fct, 3800 id_fct, 2 line_jano, 800 id_jano FROM DUAL UNION ALL
    SELECT 'EASY PRADO MEDELLIN (3806)' store_desc, 4 line_fct, 3806 id_fct, 2 line_jano, 806 id_jano FROM DUAL UNION ALL
    SELECT 'EASY SOACHA (3812)' store_desc, 4 line_fct, 3812 id_fct, 2 line_jano, 812 id_jano FROM DUAL UNION ALL
    SELECT 'EDS 1 MAYO (8)' store_desc, 3 line_fct, 8 id_fct, 1 line_jano, 8 id_jano FROM DUAL UNION ALL
    SELECT 'EDS ALAMOS (139)' store_desc, 3 line_fct, 139 id_fct, 1 line_jano, 139 id_jano FROM DUAL UNION ALL
    SELECT 'EDS ALQUERIA (149)' store_desc, 3 line_fct, 149 id_fct, 1 line_jano, 149 id_jano FROM DUAL UNION ALL
    SELECT 'EDS APOLO AUTOSUR (21)' store_desc, 3 line_fct, 21 id_fct, 1 line_jano, 21 id_jano FROM DUAL UNION ALL
    SELECT 'EDS AV DEL RIO (98)' store_desc, 3 line_fct, 98 id_fct, 1 line_jano, 98 id_jano FROM DUAL UNION ALL
    SELECT 'EDS AVD CIUDAD CALI (145)' store_desc, 3 line_fct, 145 id_fct, 1 line_jano, 145 id_jano FROM DUAL UNION ALL
    SELECT 'EDS BAHIA CL 46 (136)' store_desc, 3 line_fct, 136 id_fct, 1 line_jano, 136 id_jano FROM DUAL UNION ALL
    SELECT 'EDS CALLE 190 (161)' store_desc, 3 line_fct, 161 id_fct, 1 line_jano, 161 id_jano FROM DUAL UNION ALL
    SELECT 'EDS COLOMBIA CALLE 50 (7)' store_desc, 3 line_fct, 7 id_fct, 1 line_jano, 7 id_jano FROM DUAL UNION ALL
    SELECT 'EDS IVESUR CIRCUN (123)' store_desc, 3 line_fct, 123 id_fct, 1 line_jano, 123 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 17 CRA 17 (159)' store_desc, 3 line_fct, 159 id_fct, 1 line_jano, 159 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 24 CL 5B (132)' store_desc, 3 line_fct, 132 id_fct, 1 line_jano, 132 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 42 CL 34B (158)' store_desc, 3 line_fct, 158 id_fct, 1 line_jano, 158 id_jano FROM DUAL UNION ALL
    SELECT 'EDS MARRUECOS (2)' store_desc, 3 line_fct, 2 id_fct, 1 line_jano, 2 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SAN GABRIEL AERO (133)' store_desc, 3 line_fct, 133 id_fct, 1 line_jano, 133 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SEVILLANA (146)' store_desc, 3 line_fct, 146 id_fct, 1 line_jano, 146 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SIMON BOLIVAR CL 25 (134)' store_desc, 3 line_fct, 134 id_fct, 1 line_jano, 134 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SOACHA TERRENOS (160)' store_desc, 3 line_fct, 160 id_fct, 1 line_jano, 160 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TERCERA CL 34 (125)' store_desc, 3 line_fct, 125 id_fct, 1 line_jano, 125 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TINTALITO (101)' store_desc, 3 line_fct, 101 id_fct, 1 line_jano, 101 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TREBOL CL 76 (121)' store_desc, 3 line_fct, 121 id_fct, 1 line_jano, 121 id_jano FROM DUAL UNION ALL
    SELECT 'EDS YUMBO CRA 33 (102)' store_desc, 3 line_fct, 102 id_fct, 1 line_jano, 102 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO 20 DE JULIO (17)' store_desc, 2 line_fct, 17 id_fct, 1 line_jano, 17 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ALTOS DEL COUNTRY (249)' store_desc, 1 line_fct, 249 id_fct, 1 line_jano, 249 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ALTOS DEL PRADO (43)' store_desc, 1 line_fct, 43 id_fct, 1 line_jano, 43 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO AMERICANO (86)' store_desc, 1 line_fct, 86 id_fct, 1 line_jano, 86 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ATLANTIS (194)' store_desc, 1 line_fct, 194 id_fct, 1 line_jano, 194 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ATRIO (253)' store_desc, 1 line_fct, 253 id_fct, 1 line_jano, 253 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO AUTOPISTA SUR (18)' store_desc, 1 line_fct, 18 id_fct, 1 line_jano, 18 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO BUENAVISTA (88)' store_desc, 1 line_fct, 88 id_fct, 1 line_jano, 88 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO BULEVAR NIZA (3)' store_desc, 1 line_fct, 3 id_fct, 1 line_jano, 3 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CABECERA (103)' store_desc, 1 line_fct, 103 id_fct, 1 line_jano, 103 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CALLE 170 (14)' store_desc, 1 line_fct, 14 id_fct, 1 line_jano, 14 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CALLE 80 (11)' store_desc, 1 line_fct, 11 id_fct, 1 line_jano, 11 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CANAVERALL (108)' store_desc, 1 line_fct, 108 id_fct, 1 line_jano, 108 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CARIBE PLAZA (83)' store_desc, 1 line_fct, 83 id_fct, 1 line_jano, 83 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CARRERA 30 (16)' store_desc, 1 line_fct, 16 id_fct, 1 line_jano, 16 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIA (44)' store_desc, 1 line_fct, 44 id_fct, 1 line_jano, 44 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIA BAZAR (191)' store_desc, 1 line_fct, 191 id_fct, 1 line_jano, 191 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIPICHAPE (31)' store_desc, 1 line_fct, 31 id_fct, 1 line_jano, 31 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO DE LA 65 (23)' store_desc, 1 line_fct, 23 id_fct, 1 line_jano, 23 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO EL CASTILLO (174)' store_desc, 1 line_fct, 174 id_fct, 1 line_jano, 174 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO GIRARDOT (47)' store_desc, 1 line_fct, 47 id_fct, 1 line_jano, 47 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO GUATAPURI (87)' store_desc, 1 line_fct, 87 id_fct, 1 line_jano, 87 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO HAYUELOS (15)' store_desc, 1 line_fct, 15 id_fct, 1 line_jano, 15 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO LAS VEGAS (22)' store_desc, 1 line_fct, 22 id_fct, 1 line_jano, 22 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO LIMONAR PREMIER (30)' store_desc, 1 line_fct, 30 id_fct, 1 line_jano, 30 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO MEGA MALL (84)' store_desc, 1 line_fct, 84 id_fct, 1 line_jano, 84 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PASTO (128)' store_desc, 2 line_fct, 128 id_fct, 1 line_jano, 128 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PLAZA CENTRAL (193)' store_desc, 1 line_fct, 193 id_fct, 1 line_jano, 193 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO POPAYAN (36)' store_desc, 1 line_fct, 36 id_fct, 1 line_jano, 36 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PREMIUM PLAZA (24)' store_desc, 1 line_fct, 24 id_fct, 1 line_jano, 24 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO RIONEGRO (27)' store_desc, 1 line_fct, 27 id_fct, 1 line_jano, 27 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SAN SILVESTRE (126)' store_desc, 1 line_fct, 126 id_fct, 1 line_jano, 126 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA ANA (19)' store_desc, 1 line_fct, 19 id_fct, 1 line_jano, 19 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA FE (72)' store_desc, 1 line_fct, 72 id_fct, 1 line_jano, 72 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA MARTA (45)' store_desc, 1 line_fct, 45 id_fct, 1 line_jano, 45 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTAFE (148)' store_desc, 1 line_fct, 148 id_fct, 1 line_jano, 148 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SOACHA (48)' store_desc, 2 line_fct, 48 id_fct, 1 line_jano, 48 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SUBA (70)' store_desc, 1 line_fct, 70 id_fct, 1 line_jano, 70 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO TITAN (167)' store_desc, 1 line_fct, 167 id_fct, 1 line_jano, 167 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO TUNJA (76)' store_desc, 1 line_fct, 76 id_fct, 1 line_jano, 76 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO UNICENTRO (9)' store_desc, 1 line_fct, 9 id_fct, 1 line_jano, 9 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO VALLE DE LILI (13)' store_desc, 1 line_fct, 13 id_fct, 1 line_jano, 13 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO YOPAL (185)' store_desc, 1 line_fct, 185 id_fct, 1 line_jano, 185 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FATELARES (806)' store_desc, 2 line_fct, 806 id_fct, 1 line_jano, 806 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FONTIBON (78)' store_desc, 2 line_fct, 78 id_fct, 1 line_jano, 78 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MAYALES (184)' store_desc, 2 line_fct, 184 id_fct, 1 line_jano, 184 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ALQUERIA (124)' store_desc, 2 line_fct, 124 id_fct, 1 line_jano, 124 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ATALAYAS (82)' store_desc, 2 line_fct, 82 id_fct, 1 line_jano, 82 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BANDERAS (26)' store_desc, 2 line_fct, 26 id_fct, 1 line_jano, 26 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BELLO ANTIOQUIA (25)' store_desc, 2 line_fct, 25 id_fct, 1 line_jano, 25 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BOSA (10)' store_desc, 2 line_fct, 10 id_fct, 1 line_jano, 10 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BUGA (35)' store_desc, 2 line_fct, 35 id_fct, 1 line_jano, 35 id_jano FROM DUAL UNION ALL
    SELECT 'METRO CARTAGO (33)' store_desc, 2 line_fct, 33 id_fct, 1 line_jano, 33 id_jano FROM DUAL UNION ALL
    SELECT 'METRO DOSQUEBRADAS (166)' store_desc, 2 line_fct, 166 id_fct, 1 line_jano, 166 id_jano FROM DUAL UNION ALL
    SELECT 'METRO DUITAMA (28)' store_desc, 2 line_fct, 28 id_fct, 1 line_jano, 28 id_jano FROM DUAL UNION ALL
    SELECT 'METRO E_COMMERCE (203)' store_desc, 3 line_fct, 203 id_fct, 1 line_jano, 203 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS ALHAMBRA (334)' store_desc, 2 line_fct, 334 id_fct, 1 line_jano, 334 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS ANT COUNTRY (305)' store_desc, 2 line_fct, 305 id_fct, 1 line_jano, 305 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 125 (340)' store_desc, 2 line_fct, 340 id_fct, 1 line_jano, 340 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 148 (329)' store_desc, 2 line_fct, 329 id_fct, 1 line_jano, 329 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 45 (309)' store_desc, 2 line_fct, 309 id_fct, 1 line_jano, 309 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 93 (324)' store_desc, 2 line_fct, 324 id_fct, 1 line_jano, 324 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 95 (303)' store_desc, 2 line_fct, 303 id_fct, 1 line_jano, 303 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CARACAS CON 49 (304)' store_desc, 2 line_fct, 304 id_fct, 1 line_jano, 304 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CARRERA 3 (336)' store_desc, 2 line_fct, 336 id_fct, 1 line_jano, 336 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CEDRITOS  CALL (301)' store_desc, 2 line_fct, 301 id_fct, 1 line_jano, 301 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CIUDAD SALITRE (337)' store_desc, 2 line_fct, 337 id_fct, 1 line_jano, 337 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CORFERIAS (333)' store_desc, 2 line_fct, 333 id_fct, 1 line_jano, 333 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS JAVERIANA 45 (335)' store_desc, 2 line_fct, 335 id_fct, 1 line_jano, 335 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FACATATIVA (74)' store_desc, 2 line_fct, 74 id_fct, 1 line_jano, 74 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FLORIDABLANCA (34)' store_desc, 2 line_fct, 34 id_fct, 1 line_jano, 34 id_jano FROM DUAL UNION ALL
    SELECT 'METRO GIRON (39)' store_desc, 2 line_fct, 39 id_fct, 1 line_jano, 39 id_jano FROM DUAL UNION ALL
    SELECT 'METRO IBAGUE (42)' store_desc, 2 line_fct, 42 id_fct, 1 line_jano, 42 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ITAGUI (46)' store_desc, 2 line_fct, 46 id_fct, 1 line_jano, 46 id_jano FROM DUAL UNION ALL
    SELECT 'METRO LA 70 (32)' store_desc, 2 line_fct, 32 id_fct, 1 line_jano, 32 id_jano FROM DUAL UNION ALL
    SELECT 'METRO LIBERTADORES (80)' store_desc, 2 line_fct, 80 id_fct, 1 line_jano, 80 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MONTERIA (85)' store_desc, 2 line_fct, 85 id_fct, 1 line_jano, 85 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MOSQUERA (73)' store_desc, 2 line_fct, 73 id_fct, 1 line_jano, 73 id_jano FROM DUAL UNION ALL
    SELECT 'METRO NEIVA (38)' store_desc, 2 line_fct, 38 id_fct, 1 line_jano, 38 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PALMIRA (6)' store_desc, 2 line_fct, 6 id_fct, 1 line_jano, 6 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PASTO UNICO (171)' store_desc, 2 line_fct, 171 id_fct, 1 line_jano, 171 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PITALITO (179)' store_desc, 2 line_fct, 179 id_fct, 1 line_jano, 179 id_jano FROM DUAL UNION ALL
    SELECT 'METRO RIOHACHA (40)' store_desc, 2 line_fct, 40 id_fct, 1 line_jano, 40 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SAN CAYETANO (79)' store_desc, 2 line_fct, 79 id_fct, 1 line_jano, 79 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SAN GIL (183)' store_desc, 2 line_fct, 183 id_fct, 1 line_jano, 183 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SANTA LUCIA (195)' store_desc, 2 line_fct, 195 id_fct, 1 line_jano, 195 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SIMON BOLIVAR (75)' store_desc, 2 line_fct, 75 id_fct, 1 line_jano, 75 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SOGAMOSO (97)' store_desc, 2 line_fct, 97 id_fct, 1 line_jano, 97 id_jano FROM DUAL UNION ALL
    SELECT 'METRO TINTALITO (71)' store_desc, 2 line_fct, 71 id_fct, 1 line_jano, 71 id_jano FROM DUAL UNION ALL
    SELECT 'METRO VENTURA (81)' store_desc, 2 line_fct, 81 id_fct, 1 line_jano, 81 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ZIPAQUIRA (77)' store_desc, 2 line_fct, 77 id_fct, 1 line_jano, 77 id_jano FROM DUAL
)
SELECT
    TO_CHAR(tr.id_tra) id_tra,
    vp.tpo_fctra_vep tipo_tr,
    tr.estdo_tra estado,
    TRIM(vp.prfjo_fctra_vep) prefijo_jan,
    TRIM(vp.fctra_vep) consecutivo_jan,
    TRIM(vp.prfjo_fctra_vep) || TRIM(vp.fctra_vep) factura_jan,
    TO_CHAR(es.line_jano) line_jan,
    es.store_desc tienda_desc_jan,
    TO_CHAR(es.id_fct) tienda_jan,
    TO_CHAR(tr.pos_tra) caja_jan,
    TO_CHAR(tr.transccion_tra) trx_jan,
    TO_CHAR(tr.fcha_crre_fdc, 'YYYY-MM-DD') fecha_cierre,
    TO_CHAR(tr.fcha_incia_tra, 'YYYY-MM-DD') fecha_ini,
    TO_CHAR(tr.fcha_fnlza_tra, 'YYYY-MM-DD') fecha_fin,
    TO_CHAR(vp.vlor_pgdo_vep) valor_jan,
    vp.id_clie cliente_jan,
    vp.tpo_id_clie tipo_identificacion,
    tr.id_cnal_vnta canal
FROM
    equivalent_store es
        INNER JOIN jano.trnsccion tr ON (
        es.line_jano = tr.id_neg
            AND es.id_jano = tr.id_tie
        )
        INNER JOIN jano.vntas_pos vp ON (
        tr.id_tra = vp.id_tra
            AND tr.id_neg = vp.id_neg
        )
WHERE
    tr.fcha_crre_fdc BETWEEN TO_DATE('{start_date}', 'YYYY-MM-DD') AND TO_DATE('{end_date}', 'YYYY-MM-DD')
  AND tr.estdo_tra IN ('A', 'E')
  AND tr.id_neg IN (1, 2)
  AND es.id_fct = {store}
  AND tr.pos_tra = {pos}
  AND tr.transccion_tra = {trx}"""


PAIR_NT_JAN_SQL = """WITH equivalent_store AS (
    SELECT 'CABECERA (322)' store_desc, 2 line_fct, 322 id_fct, 1 line_jano, 322 id_jano FROM DUAL UNION ALL
    SELECT 'E_COMMERCE (204)' store_desc, 3 line_fct, 204 id_fct, 1 line_jano, 204 id_jano FROM DUAL UNION ALL
    SELECT 'EASY 4SUR MEDELLIN (3814)' store_desc, 4 line_fct, 3814 id_fct, 2 line_jano, 814 id_jano FROM DUAL UNION ALL
    SELECT 'EASY ALTOS DEL PRADO (3043)' store_desc, 4 line_fct, 3043 id_fct, 2 line_jano, 43 id_jano FROM DUAL UNION ALL
    SELECT 'EASY AMERICAS (5)' store_desc, 4 line_fct, 5 id_fct, 2 line_jano, 802 id_jano FROM DUAL UNION ALL
    SELECT 'EASY AUTOSUR (1006)' store_desc, 4 line_fct, 1006 id_fct, 2 line_jano, 18 id_jano FROM DUAL UNION ALL
    SELECT 'EASY BOSA (1002)' store_desc, 4 line_fct, 1002 id_fct, 2 line_jano, 10 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 13 (3811)' store_desc, 4 line_fct, 3811 id_fct, 2 line_jano, 811 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 170 (3014)' store_desc, 4 line_fct, 3014 id_fct, 2 line_jano, 14 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CALLE 80 (1004)' store_desc, 4 line_fct, 1004 id_fct, 2 line_jano, 11 id_jano FROM DUAL UNION ALL
    SELECT 'EASY CENTRO MAYOR (3805)' store_desc, 4 line_fct, 3805 id_fct, 2 line_jano, 805 id_jano FROM DUAL UNION ALL
    SELECT 'EASY GAITAN CORTES (3813)' store_desc, 4 line_fct, 3813 id_fct, 2 line_jano, 813 id_jano FROM DUAL UNION ALL
    SELECT 'EASY HAYUELOS (12)' store_desc, 4 line_fct, 12 id_fct, 2 line_jano, 15 id_jano FROM DUAL UNION ALL
    SELECT 'EASY MAYALES VALLEDUPAR (3809)' store_desc, 4 line_fct, 3809 id_fct, 2 line_jano, 809 id_jano FROM DUAL UNION ALL
    SELECT 'EASY NORTE (3801)' store_desc, 4 line_fct, 3801 id_fct, 2 line_jano, 801 id_jano FROM DUAL UNION ALL
    SELECT 'EASY OCCIDENTE (3800)' store_desc, 4 line_fct, 3800 id_fct, 2 line_jano, 800 id_jano FROM DUAL UNION ALL
    SELECT 'EASY PRADO MEDELLIN (3806)' store_desc, 4 line_fct, 3806 id_fct, 2 line_jano, 806 id_jano FROM DUAL UNION ALL
    SELECT 'EASY SOACHA (3812)' store_desc, 4 line_fct, 3812 id_fct, 2 line_jano, 812 id_jano FROM DUAL UNION ALL
    SELECT 'EDS 1 MAYO (8)' store_desc, 3 line_fct, 8 id_fct, 1 line_jano, 8 id_jano FROM DUAL UNION ALL
    SELECT 'EDS ALAMOS (139)' store_desc, 3 line_fct, 139 id_fct, 1 line_jano, 139 id_jano FROM DUAL UNION ALL
    SELECT 'EDS ALQUERIA (149)' store_desc, 3 line_fct, 149 id_fct, 1 line_jano, 149 id_jano FROM DUAL UNION ALL
    SELECT 'EDS APOLO AUTOSUR (21)' store_desc, 3 line_fct, 21 id_fct, 1 line_jano, 21 id_jano FROM DUAL UNION ALL
    SELECT 'EDS AV DEL RIO (98)' store_desc, 3 line_fct, 98 id_fct, 1 line_jano, 98 id_jano FROM DUAL UNION ALL
    SELECT 'EDS AVD CIUDAD CALI (145)' store_desc, 3 line_fct, 145 id_fct, 1 line_jano, 145 id_jano FROM DUAL UNION ALL
    SELECT 'EDS BAHIA CL 46 (136)' store_desc, 3 line_fct, 136 id_fct, 1 line_jano, 136 id_jano FROM DUAL UNION ALL
    SELECT 'EDS CALLE 190 (161)' store_desc, 3 line_fct, 161 id_fct, 1 line_jano, 161 id_jano FROM DUAL UNION ALL
    SELECT 'EDS COLOMBIA CALLE 50 (7)' store_desc, 3 line_fct, 7 id_fct, 1 line_jano, 7 id_jano FROM DUAL UNION ALL
    SELECT 'EDS IVESUR CIRCUN (123)' store_desc, 3 line_fct, 123 id_fct, 1 line_jano, 123 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 17 CRA 17 (159)' store_desc, 3 line_fct, 159 id_fct, 1 line_jano, 159 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 24 CL 5B (132)' store_desc, 3 line_fct, 132 id_fct, 1 line_jano, 132 id_jano FROM DUAL UNION ALL
    SELECT 'EDS LA 42 CL 34B (158)' store_desc, 3 line_fct, 158 id_fct, 1 line_jano, 158 id_jano FROM DUAL UNION ALL
    SELECT 'EDS MARRUECOS (2)' store_desc, 3 line_fct, 2 id_fct, 1 line_jano, 2 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SAN GABRIEL AERO (133)' store_desc, 3 line_fct, 133 id_fct, 1 line_jano, 133 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SEVILLANA (146)' store_desc, 3 line_fct, 146 id_fct, 1 line_jano, 146 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SIMON BOLIVAR CL 25 (134)' store_desc, 3 line_fct, 134 id_fct, 1 line_jano, 134 id_jano FROM DUAL UNION ALL
    SELECT 'EDS SOACHA TERRENOS (160)' store_desc, 3 line_fct, 160 id_fct, 1 line_jano, 160 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TERCERA CL 34 (125)' store_desc, 3 line_fct, 125 id_fct, 1 line_jano, 125 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TINTALITO (101)' store_desc, 3 line_fct, 101 id_fct, 1 line_jano, 101 id_jano FROM DUAL UNION ALL
    SELECT 'EDS TREBOL CL 76 (121)' store_desc, 3 line_fct, 121 id_fct, 1 line_jano, 121 id_jano FROM DUAL UNION ALL
    SELECT 'EDS YUMBO CRA 33 (102)' store_desc, 3 line_fct, 102 id_fct, 1 line_jano, 102 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO 20 DE JULIO (17)' store_desc, 2 line_fct, 17 id_fct, 1 line_jano, 17 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ALTOS DEL COUNTRY (249)' store_desc, 1 line_fct, 249 id_fct, 1 line_jano, 249 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ALTOS DEL PRADO (43)' store_desc, 1 line_fct, 43 id_fct, 1 line_jano, 43 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO AMERICANO (86)' store_desc, 1 line_fct, 86 id_fct, 1 line_jano, 86 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ATLANTIS (194)' store_desc, 1 line_fct, 194 id_fct, 1 line_jano, 194 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO ATRIO (253)' store_desc, 1 line_fct, 253 id_fct, 1 line_jano, 253 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO AUTOPISTA SUR (18)' store_desc, 1 line_fct, 18 id_fct, 1 line_jano, 18 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO BUENAVISTA (88)' store_desc, 1 line_fct, 88 id_fct, 1 line_jano, 88 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO BULEVAR NIZA (3)' store_desc, 1 line_fct, 3 id_fct, 1 line_jano, 3 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CABECERA (103)' store_desc, 1 line_fct, 103 id_fct, 1 line_jano, 103 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CALLE 170 (14)' store_desc, 1 line_fct, 14 id_fct, 1 line_jano, 14 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CALLE 80 (11)' store_desc, 1 line_fct, 11 id_fct, 1 line_jano, 11 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CANAVERALL (108)' store_desc, 1 line_fct, 108 id_fct, 1 line_jano, 108 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CARIBE PLAZA (83)' store_desc, 1 line_fct, 83 id_fct, 1 line_jano, 83 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CARRERA 30 (16)' store_desc, 1 line_fct, 16 id_fct, 1 line_jano, 16 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIA (44)' store_desc, 1 line_fct, 44 id_fct, 1 line_jano, 44 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIA BAZAR (191)' store_desc, 1 line_fct, 191 id_fct, 1 line_jano, 191 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO CHIPICHAPE (31)' store_desc, 1 line_fct, 31 id_fct, 1 line_jano, 31 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO DE LA 65 (23)' store_desc, 1 line_fct, 23 id_fct, 1 line_jano, 23 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO EL CASTILLO (174)' store_desc, 1 line_fct, 174 id_fct, 1 line_jano, 174 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO GIRARDOT (47)' store_desc, 1 line_fct, 47 id_fct, 1 line_jano, 47 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO GUATAPURI (87)' store_desc, 1 line_fct, 87 id_fct, 1 line_jano, 87 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO HAYUELOS (15)' store_desc, 1 line_fct, 15 id_fct, 1 line_jano, 15 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO LAS VEGAS (22)' store_desc, 1 line_fct, 22 id_fct, 1 line_jano, 22 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO LIMONAR PREMIER (30)' store_desc, 1 line_fct, 30 id_fct, 1 line_jano, 30 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO MEGA MALL (84)' store_desc, 1 line_fct, 84 id_fct, 1 line_jano, 84 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PASTO (128)' store_desc, 2 line_fct, 128 id_fct, 1 line_jano, 128 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PLAZA CENTRAL (193)' store_desc, 1 line_fct, 193 id_fct, 1 line_jano, 193 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO POPAYAN (36)' store_desc, 1 line_fct, 36 id_fct, 1 line_jano, 36 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO PREMIUM PLAZA (24)' store_desc, 1 line_fct, 24 id_fct, 1 line_jano, 24 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO RIONEGRO (27)' store_desc, 1 line_fct, 27 id_fct, 1 line_jano, 27 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SAN SILVESTRE (126)' store_desc, 1 line_fct, 126 id_fct, 1 line_jano, 126 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA ANA (19)' store_desc, 1 line_fct, 19 id_fct, 1 line_jano, 19 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA FE (72)' store_desc, 1 line_fct, 72 id_fct, 1 line_jano, 72 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTA MARTA (45)' store_desc, 1 line_fct, 45 id_fct, 1 line_jano, 45 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SANTAFE (148)' store_desc, 1 line_fct, 148 id_fct, 1 line_jano, 148 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SOACHA (48)' store_desc, 2 line_fct, 48 id_fct, 1 line_jano, 48 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO SUBA (70)' store_desc, 1 line_fct, 70 id_fct, 1 line_jano, 70 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO TITAN (167)' store_desc, 1 line_fct, 167 id_fct, 1 line_jano, 167 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO TUNJA (76)' store_desc, 1 line_fct, 76 id_fct, 1 line_jano, 76 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO UNICENTRO (9)' store_desc, 1 line_fct, 9 id_fct, 1 line_jano, 9 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO VALLE DE LILI (13)' store_desc, 1 line_fct, 13 id_fct, 1 line_jano, 13 id_jano FROM DUAL UNION ALL
    SELECT 'JUMBO YOPAL (185)' store_desc, 1 line_fct, 185 id_fct, 1 line_jano, 185 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FATELARES (806)' store_desc, 2 line_fct, 806 id_fct, 1 line_jano, 806 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FONTIBON (78)' store_desc, 2 line_fct, 78 id_fct, 1 line_jano, 78 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MAYALES (184)' store_desc, 2 line_fct, 184 id_fct, 1 line_jano, 184 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ALQUERIA (124)' store_desc, 2 line_fct, 124 id_fct, 1 line_jano, 124 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ATALAYAS (82)' store_desc, 2 line_fct, 82 id_fct, 1 line_jano, 82 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BANDERAS (26)' store_desc, 2 line_fct, 26 id_fct, 1 line_jano, 26 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BELLO ANTIOQUIA (25)' store_desc, 2 line_fct, 25 id_fct, 1 line_jano, 25 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BOSA (10)' store_desc, 2 line_fct, 10 id_fct, 1 line_jano, 10 id_jano FROM DUAL UNION ALL
    SELECT 'METRO BUGA (35)' store_desc, 2 line_fct, 35 id_fct, 1 line_jano, 35 id_jano FROM DUAL UNION ALL
    SELECT 'METRO CARTAGO (33)' store_desc, 2 line_fct, 33 id_fct, 1 line_jano, 33 id_jano FROM DUAL UNION ALL
    SELECT 'METRO DOSQUEBRADAS (166)' store_desc, 2 line_fct, 166 id_fct, 1 line_jano, 166 id_jano FROM DUAL UNION ALL
    SELECT 'METRO DUITAMA (28)' store_desc, 2 line_fct, 28 id_fct, 1 line_jano, 28 id_jano FROM DUAL UNION ALL
    SELECT 'METRO E_COMMERCE (203)' store_desc, 3 line_fct, 203 id_fct, 1 line_jano, 203 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS ALHAMBRA (334)' store_desc, 2 line_fct, 334 id_fct, 1 line_jano, 334 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS ANT COUNTRY (305)' store_desc, 2 line_fct, 305 id_fct, 1 line_jano, 305 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 125 (340)' store_desc, 2 line_fct, 340 id_fct, 1 line_jano, 340 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 148 (329)' store_desc, 2 line_fct, 329 id_fct, 1 line_jano, 329 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 45 (309)' store_desc, 2 line_fct, 309 id_fct, 1 line_jano, 309 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 93 (324)' store_desc, 2 line_fct, 324 id_fct, 1 line_jano, 324 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CALLE 95 (303)' store_desc, 2 line_fct, 303 id_fct, 1 line_jano, 303 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CARACAS CON 49 (304)' store_desc, 2 line_fct, 304 id_fct, 1 line_jano, 304 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CARRERA 3 (336)' store_desc, 2 line_fct, 336 id_fct, 1 line_jano, 336 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CEDRITOS  CALL (301)' store_desc, 2 line_fct, 301 id_fct, 1 line_jano, 301 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CIUDAD SALITRE (337)' store_desc, 2 line_fct, 337 id_fct, 1 line_jano, 337 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS CORFERIAS (333)' store_desc, 2 line_fct, 333 id_fct, 1 line_jano, 333 id_jano FROM DUAL UNION ALL
    SELECT 'METRO EXPRESS JAVERIANA 45 (335)' store_desc, 2 line_fct, 335 id_fct, 1 line_jano, 335 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FACATATIVA (74)' store_desc, 2 line_fct, 74 id_fct, 1 line_jano, 74 id_jano FROM DUAL UNION ALL
    SELECT 'METRO FLORIDABLANCA (34)' store_desc, 2 line_fct, 34 id_fct, 1 line_jano, 34 id_jano FROM DUAL UNION ALL
    SELECT 'METRO GIRON (39)' store_desc, 2 line_fct, 39 id_fct, 1 line_jano, 39 id_jano FROM DUAL UNION ALL
    SELECT 'METRO IBAGUE (42)' store_desc, 2 line_fct, 42 id_fct, 1 line_jano, 42 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ITAGUI (46)' store_desc, 2 line_fct, 46 id_fct, 1 line_jano, 46 id_jano FROM DUAL UNION ALL
    SELECT 'METRO LA 70 (32)' store_desc, 2 line_fct, 32 id_fct, 1 line_jano, 32 id_jano FROM DUAL UNION ALL
    SELECT 'METRO LIBERTADORES (80)' store_desc, 2 line_fct, 80 id_fct, 1 line_jano, 80 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MONTERIA (85)' store_desc, 2 line_fct, 85 id_fct, 1 line_jano, 85 id_jano FROM DUAL UNION ALL
    SELECT 'METRO MOSQUERA (73)' store_desc, 2 line_fct, 73 id_fct, 1 line_jano, 73 id_jano FROM DUAL UNION ALL
    SELECT 'METRO NEIVA (38)' store_desc, 2 line_fct, 38 id_fct, 1 line_jano, 38 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PALMIRA (6)' store_desc, 2 line_fct, 6 id_fct, 1 line_jano, 6 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PASTO UNICO (171)' store_desc, 2 line_fct, 171 id_fct, 1 line_jano, 171 id_jano FROM DUAL UNION ALL
    SELECT 'METRO PITALITO (179)' store_desc, 2 line_fct, 179 id_fct, 1 line_jano, 179 id_jano FROM DUAL UNION ALL
    SELECT 'METRO RIOHACHA (40)' store_desc, 2 line_fct, 40 id_fct, 1 line_jano, 40 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SAN CAYETANO (79)' store_desc, 2 line_fct, 79 id_fct, 1 line_jano, 79 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SAN GIL (183)' store_desc, 2 line_fct, 183 id_fct, 1 line_jano, 183 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SANTA LUCIA (195)' store_desc, 2 line_fct, 195 id_fct, 1 line_jano, 195 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SIMON BOLIVAR (75)' store_desc, 2 line_fct, 75 id_fct, 1 line_jano, 75 id_jano FROM DUAL UNION ALL
    SELECT 'METRO SOGAMOSO (97)' store_desc, 2 line_fct, 97 id_fct, 1 line_jano, 97 id_jano FROM DUAL UNION ALL
    SELECT 'METRO TINTALITO (71)' store_desc, 2 line_fct, 71 id_fct, 1 line_jano, 71 id_jano FROM DUAL UNION ALL
    SELECT 'METRO VENTURA (81)' store_desc, 2 line_fct, 81 id_fct, 1 line_jano, 81 id_jano FROM DUAL UNION ALL
    SELECT 'METRO ZIPAQUIRA (77)' store_desc, 2 line_fct, 77 id_fct, 1 line_jano, 77 id_jano FROM DUAL
)
SELECT
    TO_CHAR(tr.id_tra) id_tra,
    tr.id_ttr tipo_tr,
    tr.estdo_tra estado,
    TRIM(dp.prfjo_fctra_ddp) prefijo_jan,
    TRIM(dp.fctra_ddp) consecutivo_jan,
    TRIM(dp.prfjo_fctra_ddp) || TRIM(dp.fctra_ddp) AS factura_jan,
    TO_CHAR(es.line_jano) line_jan,
    es.store_desc tienda_desc_jan,
    TO_CHAR(es.id_fct) tienda_jan,
    TO_CHAR(tr.pos_tra) caja_jan,
    TO_CHAR(tr.transccion_tra) trx_jan,
    TO_CHAR(tr.fcha_crre_fdc, 'YYYY-MM-DD') fecha_cierre,
    TO_CHAR(tr.fcha_incia_tra, 'YYYY-MM-DD') fecha_ini,
    TO_CHAR(tr.fcha_fnlza_tra, 'YYYY-MM-DD') fecha_fin,
    '-' || TO_CHAR(dp.vlor_entrgdo_dep) valor_jan,
    dp.id_clie cliente_jan,
    dp.tpo_id_clie tipo_identificacion,
    tr.id_cnal_vnta canal
FROM
    equivalent_store es
        INNER JOIN jano.trnsccion tr ON (
        es.line_jano = tr.id_neg
            AND es.id_jano = tr.id_tie
        )
        INNER JOIN jano.dvlcnes_pos dp ON (
        tr.id_tra = dp.id_tra
            AND tr.id_neg = dp.id_neg
        )
WHERE
    tr.fcha_crre_fdc BETWEEN TO_DATE('{start_date}', 'YYYY-MM-DD') AND TO_DATE('{end_date}', 'YYYY-MM-DD')
  AND dp.tpo_fctra_ddp IN ('F', 'P')
  AND tr.id_neg IN (1, 2)
  AND dp.prfjo_fctra_ddp NOT IN ('VCPM ')
  AND es.id_fct = {store}
  AND tr.pos_tra = {pos}
  AND tr.transccion_tra = {trx}"""
