import pandas as pd
import requests
import re

def request_unipept_pept_to_lca(pept_df: pd.DataFrame,
                                seq_col: str) -> pd.DataFrame:
    """From a dataset of peptides, fetch lca taxonomy and rank from unipept
    database.

    Args:
        pept_df (pd.DataFrame): Peptide dataset.
        seq_col (str): Column with peptide sequences.

    Returns:
        pd.DataFrame: Peptide sequences with LCA taxonomy and LCA rank.
    """
    # perform global peptide search through unipept
    base_url = "http://api.unipept.ugent.be/api/v1/pept2lca.json?equate_il=true"

    # batch_size defines the amount of peptides to send to unipept in one request
    batch_size = 100
    seq_series = "&input[]=" + pept_df[seq_col].drop_duplicates()
    
    # initialize dataframe to store lca
    lca_df = pd.DataFrame(columns=[seq_col, "Global LCA", "Global LCA Rank"], dtype=object)

    # set index counter
    x = 0
    while True:
        if x+batch_size >= seq_series.size:
            peptides = [_ for _ in seq_series[x:]]
        else:
            peptides = [_ for _ in seq_series[x:x+batch_size]]

        # create url and send request to unipept
        req_str = "".join([base_url, *peptides])
        response = fetch_request(
            req_str,
            "Unipept request unsuccessfull"
            ).json()
    	
        lca_df = pd.concat(
            [
                lca_df,
                pd.DataFrame(
                    [(elem["peptide"], elem['taxon_id'], elem['taxon_rank']) for elem in response],
                    columns=[seq_col, "Global LCA", "Global LCA Rank"])
            ])
        x += batch_size

        # stop when end is reached
        if x >= seq_series.size:
            break
    return lca_df


def fetch_request(url: str) -> requests.Response:
    """Send GET request and return response object. Shows specific error message
    if server error encountered.

    Args:
        url (str): input URL.

    Raises:
        RuntimeError: Invalid response recieved from server.

    Returns:
        requests.Response: Response object
    """
    req_get = requests.get(url)

    error_msg = "Request failed: statuscode {}".format(req_get.status_code)
    
    if req_get.status_code != 200:
        raise RuntimeError(error_msg)
    return req_get


def wrangle_peptides(sequence: str,
                     ptm_filter: bool=True,
                     li_swap: bool=True) -> str:
    """Process protein sequences by removing post-translational
    modifications and/or equating Leucin and Isoleucin amino acids.

    Args:
        sequence (str): Protein or peptide sequence string
        ptm_filter (bool, optional): Remove PTM,s from sequence.
            Defaults to True.
        li_swap (bool, optional): Equate leucin and isoleucin.
            Defaults to True.

    Returns:
        str: Processed sequence string.
    """
    if ptm_filter is True:
        sequence = "".join(re.findall(r"[A-Z]+", sequence))
    if li_swap is True:
        sequence = sequence.replace("L", "I")
    return sequence
