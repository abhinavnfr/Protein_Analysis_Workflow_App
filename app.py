import streamlit as st
import fetch_fasta_sequence as fs

def main():
    st.markdown("<h1 style='color: pink;'>Protein Sequence Analysis Workflow Application</h1>", unsafe_allow_html=True)
    st.write("")
    st.subheader("Step 1: Fetch FASTA sequences from accession numbers")
    
    # Initialize session state
    if "fetching" not in st.session_state:
        st.session_state.fetching = False
    if "reset_uploader" not in st.session_state:
        st.session_state.reset_uploader = False

    # File uploader with dynamic key
    uploaded_file = st.file_uploader(
        "Choose a text file containing accession numbers", 
        type=["txt"], 
        key="uploader" if not st.session_state.reset_uploader else "uploader_reset"
    )
    
    if st.button("Fetch FASTA Sequences", disabled=st.session_state.fetching):
        if uploaded_file is not None:  # Ensure a file is uploaded
            st.session_state.fetching = True
            try:
                # Fetch the sequences
                output_file = fs.fetch_fasta_main(uploaded_file)
                st.write(f"Debug: output_file = {output_file}")  # Debug output
                
                if output_file:
                    # Attempt to open and provide download link
                    try:
                        with open(output_file, 'rb') as f:
                            st.download_button(
                                label="Download Sequences",
                                data=f,
                                file_name='sequences.fasta',
                                mime='text/plain'
                            )
                        # Reset state only after successful fetch and button render
                        st.session_state.fetching = False
                        st.session_state.reset_uploader = True
                        st.rerun()
                    except FileNotFoundError:
                        st.error(f"Error: Could not find file {output_file}")
                    except Exception as e:
                        st.error(f"Error opening file: {e}")
                else:
                    st.error("Error: No output file generated from fetch_fasta_main")
                    st.session_state.fetching = False  # Reset fetching on failure
            except Exception as e:
                st.error(f"Error in fetch_fasta_main: {e}")
                st.session_state.fetching = False  # Reset fetching on failure
        else:
            st.warning("Please upload a file before fetching sequences.")
    
    # Reset uploader state after rerun
    if st.session_state.reset_uploader and not st.session_state.fetching:
        st.session_state.reset_uploader = False
        st.rerun()
    
    # Show fetching message only when in progress
    if st.session_state.fetching:
        st.warning("Fetching in progress. Please wait...")

if __name__ == "__main__":
    main()
