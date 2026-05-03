# Changelog

## v6.5.0 (2026-04-16)
- Full 26-basin coverage: Africa, Middle East, Central Asia, South/SE Asia, Europe, Americas, Oceania
- 7 real satellite data sources: GPM IMERG V07, GRACE-FO MASCON, Sentinel-1/2, SMAP, GloFAS ERA5, Open-Meteo ERA5
- Parallel GEE data ingestion via ThreadPoolExecutor (8 workers)
- Alkhedir Transparency Deficit Index (ATDI) implementation
- HBV rainfall-runoff model with SCE-UA calibration
- REST API server (FastAPI) for programmatic access
- CLI: `hydrosovereign analyze`, `hydrosovereign fetch-gee`
- Telegram alert system for real-time monitoring

## v6.0.1 (2026-03-01)
- Initial public release
- SoftwareX paper submission
- DOI: 10.5281/zenodo.19180160
