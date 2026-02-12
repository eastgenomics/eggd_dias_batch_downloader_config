CONFIG = {
    "max_workers": 8,
    "batch_job_query": {
        "dx_desc_fields": {
            "output": True,
            "input": True,
            "project": True,
            "executableName": True
        },
        "exec_regex": r"^eggd_dias_batch",
        "files": {
            "qc_file": {
                "desc_path": [
                    "input",
                    "qc_file",
                    "$dnanexus_link"
                ]
            },
            "multiqc_report": {
                "desc_path": [
                    "input",
                    "multiqc_report",
                    "$dnanexus_link"
                ]
            }
        },
    },
    "launched_job_query": {
        "dx_desc_fields": {
            "output": True,
            "name": True
        },
        "execs": {
            "snv_reports_workflow": {
                "exec_regex": r"dias_reports.*\(SNV\)",
                "sample_name_regex": r"([^_]+-[^_]+)",
                "desc_paths": {
                    "SNV": [
                        "output",
                        "stage-rpt_generate_workbook.xlsx_report",
                        "$dnanexus_link"
                    ],
                    "athena_report": [
                        "output",
                        "stage-rpt_athena.report",
                        "$dnanexus_link"
                    ]
                }
            },
            "cnv_reports_workflow": {
                "exec_regex": r"^dias_reports.*\(CNV\)",
                "sample_name_regex": r"([^_]+-[^_]+)",
                "desc_paths": {
                    "CNV": [
                        "output",
                        "stage-cnv_generate_workbook.xlsx_report",
                        "$dnanexus_link"
                    ]

                }
            },
            "mosaic_reports": {
                "exec_regex": r"dias_reports.*\(mosaic\)",
                "sample_name_regex": r"([^_]+-[^_]+)",
                "desc_paths": {
                    "mosaic": [
                        "output",
                        "stage-rpt_generate_workbook.xlsx_report",
                        "$dnanexus_link"
                    ],
                    "athena_report": [
                        "output",
                        "stage-rpt_athena.report",
                        "$dnanexus_link"
                    ]
                }
            },
            "artemis_job": {
                "exec_regex": r"^eggd_artemis",
                "desc_paths": {
                    "artemis": [
                        "output",
                        "url_file",
                        "$dnanexus_link"
                    ]
                }
            }
        }
    },
    "filter_reports": {
        "SNV": {
            "details_key": "included"
        },
        "CNV": {
            "details_key": "variants"
        },
        "mosaic": {
            "details_key": "included"
        }
    },
    "output_config": {
        "folder_paths": {
            #"CEN": "/appdata/clingen/cg/Regional Genetics Laboratories/Molecular Genetics/Data archive/Sequencing HT/CEN/Run folders/",
            "CEN": "/home/greg/Downloads/Test_download",
            #"TWE": "/appdata/clingen/cg/Regional Genetics Laboratories/Molecular Genetics/Data archive/Sequencing HT/WES/",
            "TWE": "/home/greg/Downloads/Test_download"
        },
        "linux_prefix": "/appdata",
        "windows_prefix": r"\\clingen"
    }
}
