# Functions
read_binary_input() { # Function to ready binary input (yes/no)
    INPUT_TEXT=$1
    VAR_NAME=$2
    while [[ "${CURRENT_VAL}" != @(yes|no|y|n) ]] # Run the read statement as long as the parse-able input is not reached
    do
        read -p "$INPUT_TEXT [yes (y) / no (n)]: " $VAR_NAME
        CURRENT_VAL="${!VAR_NAME}"
    done

    CURRENT_VAL="" # Clear value for the next call
}

continue_prompt() {
    INPUT_TEXT=$1
    read -p "Do you want to continue with $INPUT_TEXT Press any key to continue........"
}

# TODO Support flags for automation

# Run code
source /etc/os-release # Get the system variables
echo "Starting initial setup up for $VARIANT" 




# Start step 1
echo """
Step 1. Adding the Flapak repositories
The following three as served as options
Flathub: A big library for common software available on flathub.org
KDEApps: The app for KDE available in flatpak format, beware these are nightly build
Gnome Nightly: The same principle, except for GNOME
"""

read_binary_input "Do you want to add the Flathub repos?" "ENABLE_FLATHUB"
read_binary_input "Do you want to add the KDEApps (nightlies) repos?" "ENABLE_KDE"
read_binary_input "Do you want to add the GNOME (nightlies) repos?" "ENABLE_GNOME"

read_binary_input "Do you want to continue with the current step (adding the marked flatpak repositories) [Flathub: $ENABLE_FLATHUB KDEApps: $ENABLE_KDE GNOME: $ENABLE_GNOME]?" "CONTINUE_STEP" # Ask user to confirm the operation

if [[ "${CONTINUE_STEP}" == @(yes|y) ]]; then
echo "Enabling chosen flatpak repositories.."
    for flatpak_repo in {"ENABLE_FLATHUB","ENABLE_KDE","ENABLE_GNOME"}
    do 
        case $flatpak_repo in
            ENABLE_FLATHUB)
                if [[ "${!flatpak_repo}" == @(y|yes) ]]; then
                    continue_prompt "adding the Flathub repo?" 
                    flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
                fi
                ;;
            ENABLE_KDE)
                if [[ "${!flatpak_repo}" == @(y|yes) ]]; then
                    continue_prompt "adding the KDEApps repo?" 
                    flatpak remote-add --if-not-exists kdeapps --from https://distribute.kde.org/kdeapps.flatpakrepo
                fi
                
                ;;
            ENABLE_GNOME)
                if [[ "${!flatpak_repo}" == @(y|yes) ]]; then
                    continue_prompt "adding the Gnome Nightly repo?" 
                    flatpak remote-add --if-not-exists gnome-nightly https://nightly.gnome.org/gnome-nightly.flatpakrepo
                fi
                ;;
        esac
    done

    case $VARIANT_ID in
    kinoite)
        echo "Adding theming overrides for $VARIANT"
        flatpak override --user --filesystem=~/.themes
        ;;

    silverblue)
        echo "Adding theming overrides for $VARIANT"
        flatpak override --user --filesystem=~/.themes --filesystem=~/.config/gtk-4.0
        ;;
    esac
fi

# Step 2 enable the RPMFusion repo use --live-patch




