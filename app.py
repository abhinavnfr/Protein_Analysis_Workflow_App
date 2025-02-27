import streamlit as st
import fetch_FASTA_sequence as fs

def main():
    st.title("Protein Sequence Analysis Workflow Application")
    st.write("")
    st.subheader("Step 1: Fetch FASTA sequences from accession numbers")
    
    # File uploader for accession numbers
    uploaded_file = st.file_uploader("Choose a text file containing accession numbers", type=["txt"])
    
    if st.button("Fetch FASTA Sequences"):
        output_file = fs.fetch_fasta_main(uploaded_file)
        if output_file:
            # Provide a download link for the user
            with open(output_file, 'rb') as f:
                st.download_button(
                    label="Download Sequences",
                    data=f,
                    file_name='sequences.fasta',
                    mime='text/plain'
                )

if __name__ == "__main__":
    main()
