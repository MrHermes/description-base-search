from flaskr.models.spermatophyta import Spermatophyta
import pandas as pd

def get_spermatophyta_details_list(spermatophyta_list: list[Spermatophyta]):
  return [spermatophyta.get_details() for spermatophyta in spermatophyta_list]

def find_spermatophyta_by_organism_name(organism_name: str) -> Spermatophyta:
  df = pd.read_csv("flaskr/data/spermatophyta.csv")
  row = df.loc[df["organism_name"] == organism_name]

  return Spermatophyta(
    row["accession"].values[0],
    row["tax_id"].values[0],
    row["organism_name"].values[0],
    row["common_name"].values[0]
  )

def get_spermatophytas_download_links(spermatophyta_list: list[Spermatophyta], filename: str="spermatophytas"):
  accessions = [spermatophyta.accession for spermatophyta in spermatophyta_list]
  accessions = ",".join(accessions)

  return f"https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/{accessions}/download?include_annotation_type=GENOME_FASTA&hydrated=FULLY_HYDRATED&filename={filename}.zip"
