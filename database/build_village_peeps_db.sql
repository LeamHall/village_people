-- name:    build_village_peeps_db.sql
-- version: 0.0.1
-- date:    20241020
-- author:  Leam Hall
-- desc:    Create the database.

.headers    on
.nullvalue  [NULL]
.echo       on

.read 'database/build_plots.sql'

.read 'database/build_temperaments.sql'

.read 'database/build_negative_traits.sql'

.read 'database/build_positive_traits.sql'

.read 'database/build_names.sql'


