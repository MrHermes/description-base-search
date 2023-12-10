class Spermatophyta:
  def __init__(self, accession, tax_id, organism_name, common_name):
    self.accession = accession
    self.tax_id = tax_id
    self.organism_name = organism_name
    self.common_name = common_name
    self.download_link = self.get_download_link()

  def get_download_link(self):
    filename = self.organism_name.replace(" ", "_")
    return f"https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/{self.accession}/download?include_annotation_type=GENOME_FASTA&hydrated=FULLY_HYDRATED&filename={filename}.zip"
  
  def get_details(self):
    return {
      "accession": self.accession,
      "tax_id": self.tax_id,
      "organism_name": self.organism_name,
      "common_name": self.common_name,
      "download_link": self.download_link
    }
  