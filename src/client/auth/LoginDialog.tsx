import Button from "@material-ui/core/Button";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogTitle from "@material-ui/core/DialogTitle";
import TextField from "@material-ui/core/TextField";
import * as React from "react";
import { IBaseProps } from "../root";

export interface IProps extends IBaseProps {
    isOpen: boolean;
    onSubmit: (username: string, password: string) => void;
    onClose: (event?: React.SyntheticEvent, reason?: string) => void;
}

export interface IState {
    username: string;
    password: string;
}

export class LoginDialog extends React.Component<IProps, IState> {

    constructor(props: IProps) {
        super(props);
        this.state = {
            username: null,
            password: null,
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.handleUsernameChange = this.handleUsernameChange.bind(this);
        this.handleKeyUp = this.handleKeyUp.bind(this);
    }

    public render() {
        return (
            <Dialog open={this.props.isOpen} onClose={this.props.onClose} aria-labelledby="form-dialog-title">
              <DialogTitle id="form-dialog-title">Login</DialogTitle>
              <DialogContent>
                <TextField
                    autoFocus={true}
                    margin="dense"
                    id="username"
                    label="username"
                    onChange={this.handleUsernameChange}
                    onKeyUp={this.handleKeyUp}
                    fullWidth={true}
                />
                <TextField
                  margin="dense"
                  id="password"
                  label="password"
                  type="password"
                  onChange={this.handlePasswordChange}
                  onKeyUp={this.handleKeyUp}
                  fullWidth={true}
                />
              </DialogContent>
              <DialogActions>
                <Button onClick={this.handleSubmit} color="primary">
                  Login
                </Button>
                <Button onClick={this.props.onClose} color="primary">
                  Cancel
                </Button>
              </DialogActions>
            </Dialog>
        );
    }

    private handleKeyUp(event: React.KeyboardEvent<HTMLInputElement>) {
        if (event.keyCode === 13) {
            this.props.onClose(event, "submit");
            this.props.onSubmit(this.state.username, this.state.password);
            event.preventDefault();
            event.stopPropagation();
        }
    }

    private handleSubmit() {
        this.props.onSubmit(this.state.username, this.state.password);
    }

    private handleUsernameChange(event: React.ChangeEvent<HTMLInputElement>) {
        this.setState({
            ...this.state,
            username: event.target.value,
        });
    }

    private handlePasswordChange(event: React.ChangeEvent<HTMLInputElement>) {
        this.setState({
            ...this.state,
            password: event.target.value,
        });
    }
}
