function [ H_decode_after,code_decode_after,tag_decode,rank_statistic ] = LT_decode_GuassianBallBins( H_receive,code_receive,H_decode_before,code_decode_before,rank_statistic,packetnum,k_n)
    tag_decode = 0;
    H_decode_after = [H_decode_before;
                      H_receive];
    code_decode_after = [code_decode_before;
                        code_receive];
                    
    [H_decode_after,code_decode_after] = Gussian(H_decode_after,code_decode_after);
    rank_H = find_rank(H_decode_after);
    rank_statistic = [rank_statistic rank_H];
    % disp("3333333333333333")
    % disp(rank_H)
    if rank_H >= (packetnum*k_n)
        tag_decode = 1;
        % disp("222222222222222222")
        % disp(packetnum)
        % disp(packetnum/k_n)
        % disp("1111111111111111")
        % disp(rank_H)
    end


end
